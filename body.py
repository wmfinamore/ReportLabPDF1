from reportlab.platypus import Table

def genBodyTable(width, height):
    
    widthList = [
        width * 0.10,
        width * 0.80,
        width * 0.10,
    ]
    
    heightList = [
        height * 0.10,
        height * 0.15,
        height * 0.35,
        height * 0.30,
        height * 0.10,
        
    ]
    
    res = Table([
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
    ],
        widthList,
        heightList)
    
    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])
    
    return res