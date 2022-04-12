from reportlab.platypus import Table


def genFooterTable(width, height):
    
    text = 'Root 66, 8543 Dubai - Tlf.: +43 78 11 41 00 - Email: palmsbeach@palms.com - www.palmshotel.com '
    res = Table([
        [text],
    ])
    
    return res