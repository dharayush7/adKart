from django.contrib import admin # type: ignore

# Register your models here.
from .models import Product,Contact

admin.site.register(Product)
admin.site.register(Contact)
