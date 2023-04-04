from django.shortcuts import render
from Seller.models import Seller
from Seller.models import Buyer
from .models import *
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

import datetime
import json
# Create your views here.
def home(request):
    return render(request, 'signin.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def searchProducts(request):
    products = Product.objects.filter(flag=0).values_list('product_name',flat=True)
    productList = list(products)
    return JsonResponse(productList, safe=False)

def product_detail(request, id):
     product = Product.objects.get(id=id)
     context = {
         'product':product
     }
     return render(request,"productdetail.html", context)

def crud(request): 
    prod=Product.objects.all()

    context={
        'prod':prod
    }
    return render(request, 'crud.html',context)

def add(request):
    if request.method == "POST":
        prod = Product()
        prod.product_name = request.POST.get('name')
        prod.category = request.POST.get('category')
        prod.cost=request.POST.get('cost')
        prod.image=request.POST.get('image')
        prod.save()
    return redirect('crud')

def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        cost = request.POST.get('cost')
        image = request.POST.get('image')

        prod = Product(
            id = id,
            product_name = name,
            category = category,
            cost = cost,
            image = image,
        )
        prod.save()
        return redirect('crud')
        
      
    return redirect(request, 'crud.html')

def edit(request):
    prod = Product.objects.all()
    context = {
        'prod' : prod,
    }
    return redirect(request, 'crud.html', context)

def delete(request, id):
    prod = Product.objects.filter(id = id)
    prod.delete()
    
    context = {
        'prod' : prod,
    }

    return redirect('crud')

def searchProduct(request):
    if request.method == "POST":
        searchedItem = request.POST.get('productsearch')
        product = Product.objects.filter(product_name__contains=searchedItem).first()
        if product:
            id=str(product.id)
            return redirect(id + '/product-detail/')
        else:
            messages.info(request, "Your search does not match with any product")
            return redirect(request.META.get('HTTP_REFERER'))
            
    return redirect(request.META.get('HTTP_REFERER'))       #return to previous page
def form(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    number = request.POST.get('number')
    cate = request.POST.get('cate')
    des = request.POST.get('des')
    type1 = request.POST.get('type1')
    filename = request.POST.get('filename')
    newinput.Database(name = name, email = email, number = number, cate = cate, des = des, type1 = type1, filename = filename)
    newinput.save()
    return render(request, 'form.html')

def saveenquiry(request):
    n = ''
    if request.method == "POST":
        name =request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        cate = request.POST.get('cate')
        des = request.POST.get('des')
        type1 = request.POST.get('type1')
        filename = request.POST.get('filename')
        en = Seller(name = name, email = email, number = number, cate = cate, des = des, type1 = type1, filename = filename)
        en.save()
        n='Data inserted'

    return render(request, 'form.html', {'n':n})

def Buyer_details(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
        en1 = Buyer(name = name, email = email, number = number, address = address)
        en1.save()
    return render(request, 'buyer_form.html')
def main(request):
    return render(request, 'main.html')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, status = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('cart:', cart)
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']

                product = Product.objects.get(id = i)
                total = (product.cost * cart[i]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'product':{
                        'id':product.id,
                        'name':product.product_name,
                        'price':product.cost,
                        'imageURL': product.imageURL,
                    },
                    'quantity':cart[i]['quantity'],
                    'get_total':total,
                }
                items.append(item)

                if product.flag == False:
                    order['shipping'] = True

            except: 
                pass
    
    # if hasattr(request.user, 'customer'): # If you have related name otherwise use customermodel
    #     customer = request.user.customer
    # else:
    #     print("error")

    context = {'items':items, 'order' : order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)

def store(request):
    products = Product.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        products= Product.objects.filter(product_name_icontains=q)
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        
        except Buyer.DoesNotExist:
            customer = Buyer.objects.create(user=request.user)
           
        order, created = Order.objects.get_or_create(customer = customer, status = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print('cart:', cart)
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']

                product = Product.objects.get(id = i)
                total = (product.cost * cart[i]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'product':{
                        'id':product.id,
                        'name':product.product_name,
                        'price':product.cost,
                        'imageURL': product.imageURL
                    },
                    'quantity':cart[i]['quantity'],
                    'get_total':total,
                }
                items.append(item)

                if product.flag == False:
                    order['shipping'] = True

            except: 
                pass

    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store.html', context)
def checkout(request):
    if request.user.is_authenticated:
       customer = request.user.customer 
       order, created = Order.objects.get_or_create(customer = customer, status = False)
       items = order.orderitem_set.all()
       cartItems = order.get_cart_items

    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:

            cart = {}
        print('cart:', cart)
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']

                product = Product.objects.get(id = i)
                total = (product.cost * cart[i]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'product':{
                        'id':product.id,
                        'name':product.product_name,
                        'price':product.cost,
                        'imageURL': product.imageURL
                    },
                    'quantity':cart[i]['quantity'],
                    'get_total':total,
                }
                items.append(item)

                if product.flag == False:
                    order['shipping'] = True

            except: 
                pass
    
    context = {'items':items, 'order' : order, 'cartItems':cartItems}
    return render(request, 'checkout.html', context)

def base(request):
    context = {}
    return render(request, 'base.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer = customer)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('item was added', safe = False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer)
       
    

    else:

        print('User is not logged in')
        print('COOKIES: ', request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']

        try:
            cart = json.loads(request.COOKIES['cart'])
        except:

            cart = {}
        print('cart:', cart)
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']

                product = Product.objects.get(id = i)
                total = (product.cost * cart[i]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'product':{
                        'id':product.id,
                        'name':product.product_name,
                        'price':product.cost,
                        'imageURL': product.imageURL
                    },
                    'quantity':cart[i]['quantity'],
                    'get_total':total,
                }
                items.append(item)

                if product.flag == False:
                    order['shipping'] = True

            except: 
                pass

            customer, created = Buyer.objects.get_or_create(
                email = email,

            )
            customer.name = name
            customer.save()
            order = Order.objects.create(
                customer = customer,
                status = False,
            )

            for item in items:
                product = Product.objects.get(id = item['product']['id'])
                orderItem = OrderItem.objects.create(
                    product = product,
                    order = order,
                    quantity = item['quantity'], 
                ) 

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.status = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode']

            )



        


    return JsonResponse('payment completed: ', safe = False)