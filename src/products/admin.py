from django.contrib import admin

from products.models import Product, Contract, CreditApplication, Manufacturer

admin.site.register(Product)
admin.site.register(Contract)
admin.site.register(CreditApplication)
admin.site.register(Manufacturer)
