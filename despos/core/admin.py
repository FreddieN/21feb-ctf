from django.contrib import admin
from .models import Product,ProductCategory, Cart, CartEntry

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(CartEntry)
admin.site.register(Cart)