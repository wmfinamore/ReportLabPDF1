from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


pdf = canvas.Canvas('report.pdf', pagesize = A4)
pdf.setTitle('Palms Hotel')

pdf.showPage()
pdf.save()
