from os import set_inheritable
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, A3, LETTER
from reportlab.platypus import Table
from .header import genHeaderTable
from .body import genBodyTable
from .footer import genFooterTable
from .utils import BASE_PATH

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

from reportlab.lib.pdfencrypt import StandardEncryption

import io

pdfmetrics.registerFont(
    TTFont('arabe', BASE_PATH / r'resources\Lateef-Regular.ttf')
)

#register jetBrains Mono font family ####################
pdfmetrics.registerFont(
    TTFont('jetBrainsMonoExtraBold', BASE_PATH / r'resources\newFont\JetBrainsMono-ExtraBold.ttf')
)

pdfmetrics.registerFont(
    TTFont('jetBrainsMonoExtraBoldItalic', BASE_PATH /  r'resources\newFont\JetBrainsMono-ExtraBoldItalic.ttf')
)

pdfmetrics.registerFont(
    TTFont('jetBrainsMonoItalic', BASE_PATH /  r'resources\newFont\JetBrainsMono-Italic.ttf')
)

pdfmetrics.registerFont(
    TTFont('jetBrainsMonoRegular', BASE_PATH /  r'resources\newFont\JetBrainsMono-Regular.ttf')
)

pdfmetrics.registerFontFamily(
    'jetBrainsMonoRegular',
    normal = 'jetBrainsMonoRegular', # must be equal to font family name
    italic = 'jetBrainsMonoItalic',
    bold = 'jetBrainsMonoExtraBold',
    boldItalic = 'jetBrainsMonoExtraBoldItalic',
)
##########################################################

def genPalmsHotelPage(pdf: canvas.Canvas, size, bookmark=False):
    
    pdf.setPageSize(size)
    
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
    pageNoText = f'Page {pageNo}'
    x = width * 0.92
    y = heightList[-1] * 0.25
    
    pdf.setFillColor('white')
    
    pdf.drawString(x, y, pageNoText)
    
    if bookmark:
        id = f'p{pageNo}'
        pdf.bookmarkPage(id)
        pdf.addOutlineEntry(pageNoText, id)
    
    pdf.showPage()
#END genPalmsHotelPage()


# generate pdf file


def CreatePDF(
    orientation='portrait', size=A4,
    userPass=None, ownerPass=None
):
    
    if type(size) == str:
        if size == 'A3':
            size = A3
        elif size == 'LETTER':
            size = LETTER
        else:
            size = A4
    
    enc = None
    if ownerPass and userPass:
        enc = StandardEncryption(userPass, ownerPass, canPrint=0)
    elif userPass:
        enc = userPass
    
    buffer = io.BytesIO()
    
    pdf = canvas.Canvas(buffer, encrypt=enc)
    pdf.setTitle('Palms Hotel')
    
    if orientation == 'portrait':
        genPalmsHotelPage(pdf, size)
    elif orientation == 'landscape':
        genPalmsHotelPage(pdf, landscape(size))
    elif orientation == 'both':
        genPalmsHotelPage(pdf, size, bookmark=True)
        genPalmsHotelPage(pdf, landscape(size), bookmark=True)
    else:
        genPalmsHotelPage(pdf, size)
    
    pdf.save()
    
    buffer.seek(0)
    
    return buffer
#END def CreatePDF

# if __name__ == '__main__':
#     CreatePDF(
#         'test.pdf',
#         orientation='both',
#         size=A3,
#         userPass='teste'
#     )