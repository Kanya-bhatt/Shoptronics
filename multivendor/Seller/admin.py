from django.contrib import admin
from Seller.models import *

# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'cate', 'des', 'type1', 'filename')

admin.site.register(Seller, SellerAdmin)  

class BuyerAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'email', 'number')

admin.site.register(Buyer, BuyerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'cost', 'image')

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'category', 'date_ordered', 'transaction_id', 'status')

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')

admin.site.register(OrderItem, OrderItemAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'status', 'payment_mode')

admin.site.register(Payment, PaymentAdmin)


    
admin.site.register(ShippingAddress)