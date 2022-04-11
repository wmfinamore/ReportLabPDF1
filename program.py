from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table


pdf = canvas.Canvas('report.pdf', pagesize = A4)
pdf.setTitle('Palms Hotel')

mainTable = Table([
    ['texto simples', 'nova coluna'],
    ['nova linha', 12546513246513]
])

mainTable.setStyle([
    ('GRID', (0, 0), (-1, -1), 1, 'red'),
    
])

mainTable.wrapOn(pdf, 0, 0)
mainTable.drawOn(pdf, 0, 0)

pdf.showPage()
pdf.save()
