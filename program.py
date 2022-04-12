from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table


pdf = canvas.Canvas('report.pdf', pagesize = A4)
pdf.setTitle('Palms Hotel')

width, height = A4

heightList = [
    height * 0.20,
    height * 0.77,
    height * 0.03,
]

mainTable = Table([
    ['header'],
    ['body'],
    ['footer']
    ],
        colWidths = width,
        rowHeights = heightList,)

mainTable.setStyle([
    ('GRID', (0, 0), (-1, -1), 1, 'red'),
    
])

mainTable.wrapOn(pdf, 0, 0)
mainTable.drawOn(pdf, 0, 0)

pdf.showPage()
pdf.save()
