from django.contrib import admin
from .models import *

admin.site.register(CustomerDetails)
admin.site.register(ContactDetails)
admin.site.register(Orders)
admin.site.register(Purchase)
admin.site.register(BillingDetails)
admin.site.register(PaymentDetails)
admin.site.register(WorkProgress)
admin.site.register(Expenses)