from django.shortcuts import render,redirect
#sayfa temizleme fonksiyonu redirect
from .forms import InvoiceForm
from .forms import InvoiceSearchForm,InvoiceUpdateForm
from .models import *


from django.contrib import messages



# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab

# Create your views here.
def home(request):
    title='welcome this is the home page'
    context= {
        "title": title,
        
    }
    
    return render(request,"home.html",context)

def add_invoice(request):
    form= InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/kayit')
    
    total_invoices=Invoice.objects.count()
    queryset=Invoice.objects.order_by('-invoice_date')[:6]
    context= {
        "form":form,
        "title":"New Invoice",
        "total_invoices": total_invoices,
        "queryset":queryset,
    }
    return render(request,"kayit.html",context)


def list_invoice(request):
    title='Fatura Listesi'
    liste= Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)
    
    """if request.method=='POST':
        liste=Invoice.objects.filter(invoice_number__icontains=form['invoice_number'].value(),name__icontains=form['name'].value())"""
    if request.method == 'POST':
        invoice_number = form['invoice_number'].value()
        name = form['name'].value()
        
    
        
    
        if invoice_number:
            liste = liste.filter(invoice_number__icontains=invoice_number)
        
        if name:
            liste = liste.filter(name__icontains=name)
        
       
    
    context= {
        "title": title,
        "liste": liste,
        "form": form,
    }
    
    #pdf dosyasi 
    if form['generate_invoice'].value() == True:
        instance = liste
        data_file = instance
        num_of_invoices = len(liste)
        message = str(num_of_invoices) + " invoices successfully generated."
        messages.success(request, message)
        def import_data(data_file):
            invoice_data = data_file
            for row in invoice_data:
                invoice_type = row.invoice_type
                invoice_number = row.invoice_number
                invoice_date = row.invoice_date
                name = row.name
                phone_number = row.phone_number
                line_one = row.line_one
                line_one_quantity = row.line_one_quantity
                line_one_unit_price = row.line_one_unit_price
                line_one_total_price = row.line_one_total_price

                line_two = row.line_two
                line_two_quantity = row.line_two_quantity
                line_two_unit_price = row.line_two_unit_price
                line_two_total_price = row.line_two_total_price

                line_three = row.line_three
                line_three_quantity = row.line_three_quantity
                line_three_unit_price = row.line_three_unit_price
                line_three_total_price = row.line_three_total_price

                line_four = row.line_four
                line_four_quantity = row.line_four_quantity
                line_four_unit_price = row.line_four_unit_price
                line_four_total_price = row.line_four_total_price

                line_five = row.line_five
                line_five_quantity = row.line_five_quantity
                line_five_unit_price = row.line_five_unit_price
                line_five_total_price = row.line_five_total_price

                line_six = row.line_six
                line_six_quantity = row.line_six_quantity
                line_six_unit_price = row.line_six_unit_price
                line_six_total_price = row.line_six_total_price

                line_seven = row.line_seven
                line_seven_quantity = row.line_seven_quantity
                line_seven_unit_price = row.line_seven_unit_price
                line_seven_total_price = row.line_seven_total_price

                line_eight = row.line_eight
                line_eight_quantity = row.line_eight_quantity
                line_eight_unit_price = row.line_eight_unit_price
                line_eight_total_price = row.line_eight_total_price

                line_nine = row.line_nine
                line_nine_quantity = row.line_nine_quantity
                line_nine_unit_price = row.line_nine_unit_price
                line_nine_total_price = row.line_nine_total_price

                line_ten = row.line_ten
                line_ten_quantity = row.line_ten_quantity
                line_ten_unit_price = row.line_ten_unit_price
                line_ten_total_price = row.line_ten_total_price
                lines = [
                            f"{line_one},{line_one_quantity},{line_one_unit_price},{line_one_total_price}",
                            f"{line_two},{line_two_quantity},{line_two_unit_price},{line_two_total_price}",
                            f"{line_three},{line_three_quantity},{line_three_unit_price},{line_three_total_price}",
                            f"{line_four},{line_four_quantity},{line_four_unit_price},{line_four_total_price}",
                            f"{line_five},{line_five_quantity},{line_five_unit_price},{line_five_total_price}",
                            f"{line_six},{line_six_quantity},{line_six_unit_price},{line_six_total_price}",
                            f"{line_seven},{line_seven_quantity},{line_seven_unit_price},{line_seven_total_price}",
                            f"{line_eight},{line_eight_quantity},{line_eight_unit_price},{line_eight_total_price}",
                            f"{line_nine},{line_nine_quantity},{line_nine_unit_price},{line_nine_total_price}",
                            f"{line_ten},{line_ten_quantity},{line_ten_unit_price},{line_ten_total_price}"]

            for i in range(0,len(lines)):
                lines[i]=str(lines[i])
            total = row.total
            pdf_file_name = str(invoice_number) + '_' + str(name) + '.pdf'
            generate_invoice(str(name), str(invoice_number), 
				lines, str(total), str(phone_number), str(invoice_date),
				str(invoice_type), pdf_file_name)
        
        
        def generate_invoice(name, invoice_number, lines, total, phone_number, invoice_date, invoice_type, pdf_file_name):
            c = canvas.Canvas(pdf_file_name)

		# image of seal
            logo = 'logo.png'
            c.drawImage(logo, 50, 700, width=500, height=120)

            c.setFont('Helvetica', 12, leading=None)
            if invoice_type == 'Receipt':
                c.drawCentredString(400, 660, "Receipt Number #:")
            elif invoice_type == 'Proforma Invoice':
                c.drawCentredString(400, 660, "Proforma Invoice #:")
            # else:
            c.drawCentredString(400, 660, str(invoice_type) + ':')
            c.setFont('Helvetica', 12, leading=None)
            invoice_number_string = str('0000' + invoice_number)
            c.drawCentredString(490, 660, invoice_number_string)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(409, 640, "Date:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(492, 641, invoice_date)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(397, 620, "Amount:")
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(484, 622, total)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(80, 660, "To:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(150, 660, name)

            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(98, 640, "Phone #:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(150, 640, phone_number)     

            c.setFont('Helvetica-Bold', 14, leading=None)
            c.drawCentredString(310, 580, str(invoice_type))
            c.drawCentredString(110, 560, "Particulars:")
            c.drawCentredString(295, 510, "__________________________________________________________")
            c.drawCentredString(295, 480, "__________________________________________________________")
            c.drawCentredString(295, 450, "__________________________________________________________")
            c.drawCentredString(295, 420, "__________________________________________________________")
            c.drawCentredString(295, 390, "__________________________________________________________")
            c.drawCentredString(295, 360, "__________________________________________________________")
            c.drawCentredString(295, 330, "__________________________________________________________")
            c.drawCentredString(295, 300, "__________________________________________________________")
            c.drawCentredString(295, 270, "__________________________________________________________")
            c.drawCentredString(295, 240, "__________________________________________________________")
            c.drawCentredString(295, 210, "__________________________________________________________")

            y_start = 510  # Initial Y coordinate for the lines
            y_step = 30    # Y coordinate difference between lines

            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(110, 520, 'URUNLER')
            c.drawCentredString(220, 520, 'MIKTAR')
            c.drawCentredString(330, 520, 'BIRIM FIYAT')
            c.drawCentredString(450, 520, 'TOPLAM')

            for i, line in enumerate(lines):
                if line != '':
                    y = y_start - i * y_step
                    line_data = line.split(',')
                    
                    c.setFont('Helvetica', 12, leading=None)
                    c.drawCentredString(110, y, line_data[0])
                    c.drawCentredString(220, y, line_data[1])
                    c.drawCentredString(330, y, line_data[2])
                    c.drawCentredString(450, y, line_data[3])    




            # TOTAL
            c.setFont('Helvetica-Bold', 20, leading=None)
            c.drawCentredString(400, 140, "TOPLAM:")
            c.setFont('Helvetica-Bold', 20, leading=None)
            c.drawCentredString(484, 140, total) 


            # SIGN
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(150, 140, "KASE-IMZA:__________________")
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(170, 120, 'MUDUR') 


            c.showPage()
            
            c.save()    

        import_data(data_file)

    
    
    return render(request,"liste.html",context)


def update_invoice(request,pk):
    queryset= Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    oldinvoice=queryset.invoice_number
    if request.method=='POST':
        form= InvoiceUpdateForm(request.POST, instance=queryset)
        
        if form.is_valid():
            queryset.guncelleme=True
            
            new_invoice = form.save(commit=False)  # Create a new instance without saving to the database yet
            new_invoice.id = None  # Set the ID to None to create a new record
            
            new_invoice.eskiinvoice=oldinvoice
            new_invoice.save()  # Save the new invoice as a new record
            messages.success(request, 'successfully Saved')
            return redirect('/liste')
    
    context = {
        'form' : form
    }
    
    return render(request, 'kayit.html', context)


def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    
    if request.method == 'POST':
        queryset.delete()
        return redirect('/liste')
    return render(request,'delete_invoice.html')