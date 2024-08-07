from django.contrib import admin # type: ignore

# Register your models here.
from .models import Product, Contact, Order, OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)