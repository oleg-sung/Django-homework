from django.contrib import admin

from .models import Product, Stock, StockProduct


class StockProductsInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address', ]
    list_filter = ['address']
    inlines = [StockProductsInline, ]
