# HTML Template to PDF in Django 

## What is pdf?

   PDF stands for "portable document format".  Essentially, the format is used when you need to save files that cannot be modified but still need to be easily shared and printed.  Today almost everyone has a version of Adobe Reader or other program on their computer that can read a PDF file.
    
   Important:  Once you have saved a document as a PDF file, you cannot convert it back to a Microsoft Office file format without specialized software or a third-party add-in.


## Requirement of pdf in Django?
   - We can create pdf for generation of Reports, Invoice, Receipts and many more…
   - Can maintain documents and share with other easily
   - No need to connect with server to check the records


Examples:

![Sales Sheet](https://paper-attachments.dropbox.com/s_CCFF4B9407711ACCCD37A4CBEB339CE44F5F26C3299E45EBD29BD2FD155B7275_1635136147576_Sales-Sheet-Template-Excel1.jpeg)
![Payment receipt](https://paper-attachments.dropbox.com/s_CCFF4B9407711ACCCD37A4CBEB339CE44F5F26C3299E45EBD29BD2FD155B7275_1635136103032_basic-payment-receipt-template-in-pdf-md.png)

![Product Price List](https://paper-attachments.dropbox.com/s_CCFF4B9407711ACCCD37A4CBEB339CE44F5F26C3299E45EBD29BD2FD155B7275_1635136355088_Product_Price_List.png)
![invoice templates](https://www.invoiceberry.com/img/homepage/free_invoice_templates/new/sub_pages/numbers/screenshot_invoiceberry_invoice_template_1.png)



## Why HTML template to PDF?
   We can create pdf with python standalone but its origin (0,0)  of content start from bottom left. 
        - Now imagine how difficult it would be to create any format. 
        - Need to to check and maintain sentence at specific coordinates. 
        - More time consuming if we wish add or remove any sentence from format.


   **Xhtml2pdf ✔️** 
        - What if we able create desired template easily and convert it to pdf. 
            The best and easy way to create format is render information on html page.
        - xhtml2pdf library helps to convert html page to pdf easily
        - xhtml2pdf uses (0,0) to denote the top left of a page, partly to maintain similarity with the HTML coordinate system.
        
# Implementation xhtml2pdf in Django project :

Documentation link - https://xhtml2pdf.readthedocs.io/en/latest/installation.html


## 1. Install  `xhtml2pdf`  through terminal: 

This is a typical Python library and is installed using pip


    #Using Python 3
    pip install --pre xhtml2pdf 
    
    #Using Python 2
    pip install xhtml2pdf

xhtml2pdf documentation:
https://xhtml2pdf.readthedocs.io/en/latest/


## 2. Create view to convert html to pdf in views.py:

Basic requirements for html to pdf - 

1. specify template name
2. send context
3. something/method which will convert html to pdf

    ```
    from django.conf import settings
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    from django.contrib.staticfiles import finders
    
    def render_pdf_view(request):
        template_path = 'user_printer.html'
        context = {'myvar': 'this is your template context'}
    
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)
    
        # create a pdf
        pisa_status = pisa.CreatePDF(
           html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
           return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response```

**Content-Dispositin**:

   In a regular HTTP response, the `**Content-Disposition**` response header is a header indicating if the content is expected to be displayed *inline* in the browser, that is, as a Web page or as part of a Web page, or as an *attachment*, that is downloaded and saved locally.


   Content-Disposition: inline
   Content-Disposition: attachment
   Content-Disposition: attachment; filename="filename.pdf"


## 3. Create html template to convert to pdf:
   Usually internal css is preferred.
   Because xhtml2pdf supports limited numbers of standard CSS properties. 
   It does not support to bootstrap.
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1 style="text-align: center;"><strong>Reports</strong></h1>
        <br>
        <h3>Invoice No. : {{invoice_no}}</h3>
        <h3>Invoice Date : {{invoice_date}}</h3>
        <h3>Item Name : {{product_name}}</h3>
        <h3>Quantity : {{quantity}}</h3>
        <h3>Net Price : {{price}}</h3>
    </body>
    </html>


## 4. Create Project level URL:


    from django.urls import path,include
    urlpatterns = [
        path('pdf/', include('generatepdf.urls')),
    ]


## 5. Create App Level URL:
    from django.urls import path
    from . import views
    urlpatterns=[
        path('generatepdf/',views.generatepdf, name='generatepdf')
    ]


## 6. Get output after hitting the url:
![](https://paper-attachments.dropbox.com/s_CCFF4B9407711ACCCD37A4CBEB339CE44F5F26C3299E45EBD29BD2FD155B7275_1635137898066_Screenshot+2021-10-25+at+10.25.32+AM.png)


 

## 7. Download as pdf :

You can download as pdf by clicking on highlighted download button

