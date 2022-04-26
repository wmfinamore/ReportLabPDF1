from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import Table
from header import genHeaderTable
from body import genBodyTable
from footer import genFooterTable

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

from reportlab.lib.pdfencrypt import StandardEncryption

pdfmetrics.registerFont(
    TTFont('arabe', r'resources\Lateef-Regular.ttf')
)

#register jetBrains Mono font family ####################
pdfmetrics.registerFont(
    TTFont('jetBrainsMonoExtraBold', r'resources\newFont\JetBrainsMono-ExtraBold.ttf')
)

pdfmetrics.registerFont(
    TTFont('jetBrainsMonoExtraBoldItalic', r'resources\newFont\JetBrainsMono-ExtraBoldItalic.ttf')
)

pdfmetrics.registerFont(
    TTFont('jetBrainsMonoItalic', r'resources\newFont\JetBrainsMono-Italic.ttf')
)

pdfmetrics.registerFont(
    TTFont('jetBrainsMonoRegular', r'resources\newFont\JetBrainsMono-Regular.ttf')
)

pdfmetrics.registerFontFamily(
    'jetBrainsMonoRegular',
    normal = 'jetBrainsMonoRegular', # must be equal to font family name
    italic = 'jetBrainsMonoItalic',
    bold = 'jetBrainsMonoExtraBold',
    boldItalic = 'jetBrainsMonoExtraBoldItalic',
)
##########################################################

def genPalmsHotelPage(pdf: canvas.Canvas, size):
    # setting width and height page
    width, height = size

    # heights list
    heightList = [
        height * 0.20,
        height * 0.77,
        height * 0.03,
    ]

    # create a table
    mainTable = Table([
        [genHeaderTable(width, heightList[0])],
        [genBodyTable(width, heightList[1])],
        [genFooterTable(width, heightList[2])]
        ],
            colWidths = width,
            
            # apply heights list
            rowHeights = heightList,)

    # defining style format for the table
    mainTable.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LEFTPADDING', (0, 0), (0, 2), 0),
        
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        
    ])

    # wrap the canvas with the table
    mainTable.wrapOn(pdf, 0, 0)
    mainTable.drawOn(pdf, 0, 0)
    
    pageNo = pdf.getPageNumber()
    x = width * 0.92
    y = heightList[-1] * 0.25
    
    pdf.setFillColor('white')
    
    pdf.drawString(x, y, f'Page {pageNo}')
    
    pdf.showPage()
#END genPalmsHotelPage()

size = A4
senc = StandardEncryption('abc', 'abc123', canPrint=0)

#define canvas to draw the report
pdf = canvas.Canvas('report.pdf', pagesize = size)#, encrypt=senc)
pdf.setTitle('Palms Hotel')


pdf.bookmarkPage('p1')
pdf.addOutlineEntry('Page 1', 'p1' )
pdf.setPageSize(landscape(size))
genPalmsHotelPage(pdf, landscape(size))
# pdf.showPage() # Page Break 

pdf.bookmarkPage('p2')
pdf.addOutlineEntry('Page 2', 'p2', level=1 )
pdf.setPageSize(size)
genPalmsHotelPage(pdf, size)
# pdf.showPage()

pdf.bookmarkPage('p3')
pdf.addOutlineEntry('Page 3', 'p3', level=1 )
genPalmsHotelPage(pdf, size)
# pdf.showPage()


# generate pdf file
pdf.save()
