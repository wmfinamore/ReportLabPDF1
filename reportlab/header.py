from turtle import left
from reportlab.platypus import Table, Image


def genHeaderTable(width, height):
    widthList = [
        width * 0.55, # col 1 - left image
        width * 0.45, # col 2 - right image
        width * 0, # text HOTEL black
        width * 0, # text HOTEL red
        width * 0, # text Arabic
    ]
    
    leftImagePath = 'resources\paradiseHotel.jpg'
    leftImageWidth = widthList[0]
    leftImage = Image(leftImagePath, leftImageWidth, height)
    
    rightImagePath = 'resources\logoParadise.png'
    rightImageWidth = widthList[1]
    rightImage = Image(rightImagePath, rightImageWidth, height,
                       kind='proportional')
    
    rightText = 'HOTEL'
    # rightList = [rightImage, rightText]
    
    res = Table([
        [leftImage, rightImage, rightText, rightText, 'فندق بالمز']
    ],
    widthList, height)
    
    res.setStyle([
        #('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (2, 0), (2, 0), 'CENTER'),# text black
        ('ALIGN', (3, 0), (3, 0), 'CENTER'),# text red
        ('ALIGN', (4, 0), (4, 0), 'CENTER'),# text Arabic
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        
        ('FONTSIZE', (2, 0), (4, 0), 20),
        ('FONTNAME', (2, 0), (3, 0), 'Helvetica-Bold'),
        ('FONTNAME', (4, 0), (4, 0), 'arabe'),
        
        ('LEFTPADDING', (2, 0), (2, 0), -widthList[1]), # text black
        ('LEFTPADDING', (3, 0), (3, 0), -widthList[1] - 2), # text red
        ('LEFTPADDING', (4, 0), (4, 0), -widthList[1]), # text Arabic
        
        ('BOTTOMPADDING', (2, 0), (2, 0), height * 0.20), # text black
        ('BOTTOMPADDING', (3, 0), (3, 0), (2+height) * 0.20), # text red
        ('BOTTOMPADDING', (4, 0), (4, 0), height * 0.05), # text arabic
        
        ('TEXTCOLOR', (2, 0), (2, 0), 'rgba(0, 0, 0, 0.8)'),
        ('TEXTCOLOR', (3, 0), (3, 0), 'red'),
        
    ])
    
    return res # res = Resultado