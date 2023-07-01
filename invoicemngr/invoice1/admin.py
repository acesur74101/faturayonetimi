from django.contrib import admin
from .models import *
from .forms import InvoiceForm
# Register your models here.
admin.site.register(Country)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'invoice_number', 'invoice_date','guncelleme','eskiinvoice']
    form = InvoiceForm
    list_filter = ['name','guncelleme']
    search_fields = ['name', 'invoice_number']
        
admin.site.register(Company)
admin.site.register(Satis)
admin.site.register(Invoice, InvoiceAdmin)
