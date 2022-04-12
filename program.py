from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from header import genHeaderTable
from body import genBodyTable
from footer import genFooterTable

#define canvas to draw the report
pdf = canvas.Canvas('report.pdf', pagesize = A4)
pdf.setTitle('Palms Hotel')

# setting width and height page
width, height = A4

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
    ('GRID', (0, 0), (-1, -1), 1, 'red'),
    
    ('LEFTPADDING', (0, 0), (0, 2), 0),
    
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    
])

# wrap the canvas with the table
mainTable.wrapOn(pdf, 0, 0)
mainTable.drawOn(pdf, 0, 0)

# apply configurations in our canvas
pdf.showPage()

# generate pdf file
pdf.save()
