from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def generatepdf(request):
    template_path='generatepdf/reports.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    context={
            'invoice_no':12345,
            'invoice_date':'24 Octomer',
            'product_name':'iphone 13',
            'quantity':22,
            'price':56000,
    }
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response