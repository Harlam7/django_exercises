from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "short_desc", "stock")
    search_fields = ("name", "short_desc")
    list_filter = ("discount_unitl", "stock")
    date_hierarchy = ("discount_unitl")

admin.site.register(Product, ProductAdmin)


