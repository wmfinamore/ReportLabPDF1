from django.urls import path
from .views import index, genPDF


urlpatterns = [
    path('', index, name='index'),
    path('generatePDF', genPDF, name='generatePDF'),
]