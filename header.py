from turtle import left
from reportlab.platypus import Table, Image


def genHeaderTable(width, height):
    widthList = [
        width * 0.55, # col 1 - left image
        width * 0.45, # col 2 - right image
        width * 0, # text
        width * 0, # text
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
        [leftImage, rightImage, rightText, rightText]
    ],
    widthList, height)
    
    res.setStyle([
        #('GRID', (0, 0), (-1, -1), 1, 'red'),
        
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 0),
        
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        
        ('FONTSIZE', (2, 0), (3, 0), 20),
        ('FONTNAME', (2, 0), (3, 0), 'Helvetica-Bold'),
        ('LEFTPADDING', (2, 0), (2, 0), -widthList[1] + 98), # text
        ('LEFTPADDING', (3, 0), (3, 0), -widthList[1]+ 97) , # text
        ('BOTTOMPADDING', (2, 0), (2, 0), 40), # text
        ('BOTTOMPADDING', (3, 0), (3, 0), 41), # text
        
        ('TEXTCOLOR', (2, 0), (2, 0), 'rgba(0, 0, 0, 0.8)'),
        ('TEXTCOLOR', (3, 0), (3, 0), 'red'),
        
    ])
    
    return res # res = Resultado