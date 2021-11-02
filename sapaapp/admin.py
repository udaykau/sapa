from django.contrib import admin
from .models import Querie, Product
# Register your models here.


class queries(admin.ModelAdmin):
    list_display = ('sno', 'Name', 'Email', 'Phone', 'date')


class product(admin.ModelAdmin):
    list_display = ('sno', 'Active', 'Product_Name', 'Minimum_Quantity', 'Price', 'date')


admin.site.register(Querie,  queries)
admin.site.register(Product,  product)
