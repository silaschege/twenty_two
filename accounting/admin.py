from django.contrib import admin
from .models import (
                    OrderInvoice,
                    OrderDebit,
                    DebitCaptain,
                    InvoiceCaptain,
                    SupplierInvoice,
                    SupplierDebit,
                    SupplierPaymentBalance,
                    SupplierBulkDebit,
                    )

# Register your models here.
admin.site.register(OrderInvoice)
admin.site.register(OrderDebit)
admin.site.register(InvoiceCaptain)
admin.site.register(DebitCaptain)
admin.site.register(SupplierInvoice)
admin.site.register(SupplierDebit)
admin.site.register(SupplierPaymentBalance)
admin.site.register(SupplierBulkDebit)

