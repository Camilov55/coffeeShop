from django.contrib import admin
from products.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ['name', 'price'] # Los datos que quiere que aparezca de al inicio
    search_fields = ['name'] # Genera un buscador de solo buscara en name del producto

admin.site.register(Product, ProductAdmin)