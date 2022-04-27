from django.shortcuts import render


def index(request):
    return render(request, 'reportingApp/index.html')

def genPDF(request):
    
    values = request.POST
    
    filename = values.get('fname', 'example.pdf')
    pagesize = values.get('pagesize', 'A4')
    orientation = values.get('orientation', 'landscape')
    userpass = values.get('userpass', '')
    onwerpass = values.get('ownerpass', '')
    return render(request, 'reportingApp/index.html')
