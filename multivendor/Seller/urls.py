from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    # path('form/', views.form, name = "form"),
    path('saveenquiry/', views.saveenquiry, name = "saveenquiry"),
    path('buyer_form/', views.Buyer_details, name = "Buyer1"),
    path('main/', views.main, name = "Main"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name = "checkout"),
    path('store/', views.store, name = "store"),
    path('base/', views.base, name = "base"),
    path('update_item/', views.updateItem, name = "update item"),
    path('process_order/', views.processOrder, name = "process_order"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('searchProduct', views.searchProduct, name = "searchProduct"),        
    path('product-list/', views.searchProducts),
    path('<int:id>/product-detail/', views.product_detail, name = "product-detail"),
    path('crud/', views.crud, name = "crud"),
    path('add/', views.add, name = "add"),
    path('edit/', views.edit, name = "edit"),
    path('update/<str:id>', views.update, name ="update"),
    path('delete/<str:id>', views.delete, name = "delete")
    # path('saveenquiry', )
    
]
