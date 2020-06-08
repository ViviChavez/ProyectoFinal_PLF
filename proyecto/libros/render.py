from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
# metodo estatico para renderizar la plantilla


def render_to_pdf(template_src, context_dict={}):

         template = get_template(template_src)
         html = template.render(context_dict)
         response = BytesIO()
        #creacion del pdf
         pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
         if not pdf.err:
             return HttpResponse(response.getvalue(), content_type='application/pdf')
         else:
             return HttpResponse("Error Rendering PDF", status=400)

