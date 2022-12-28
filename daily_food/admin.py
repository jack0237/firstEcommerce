from django.contrib import admin
from .models import Category, Product, Order, Cart

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order)
admin.site.register(Cart)

