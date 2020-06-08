from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import get_template
from .render import render_to_pdf 

class GenerarPdf(View):

    def get(self, request,*args,**kwargs):
       pdf=render_to_pdf('pdf.html')

       return HttpResponse(pdf, content_type='application/pdf')