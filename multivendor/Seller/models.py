from django.db import models
from django.contrib.auth.models import User
class Seller(models.Model):
    TYPE = (
        ('Books', 'Books' ),
        ('electronics', 'Electronic Component')
    )
    TYPE_CHOICE = (
        ('new','NEW'),
        ('second', 'SECOND_HAND'),
    )
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 30)
    number = models.CharField(max_length = 10)
    cate = models.CharField(choices = TYPE, max_length = 20, default = 'Books')
    des = models.CharField(max_length = 100)
    type1 = models.CharField(max_length=20, choices=TYPE_CHOICE, default='new')
    filename = models.ImageField(upload_to='images/')

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True, related_name='customer', related_query_name='customer')
    name = models.CharField(max_length = 50, null = True)
    email = models.EmailField(max_length = 30)
    number = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    TYPE = (
        ('Books', 'Books' ),
        ('electronics', 'Electronic Component')
    )
    product_name = models.CharField(max_length = 50)
    category = models.CharField(choices = TYPE, max_length = 20, default = 'Books')
    cost = models.DecimalField(max_digits = 7, decimal_places = 2)
    image = models.ImageField(null = True, blank = True)
    flag = models.BooleanField(default = False, null = True, blank = True)
   

    
    def __str__(self):
        return self.product_name

    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    

class Order(models.Model):
    TYPE_STATUS = (
        ('delivered', 'Delivered' ),
        ('pending', 'Pending'),
        ('waiting', 'Waiting')
    )
    customer = models.ForeignKey(Buyer, null=True, on_delete = models.SET_NULL)
    category = models.CharField(max_length = 30)
    date_ordered = models.DateTimeField(auto_now_add = True)
    transaction_id = models.CharField(max_length = 100, null = True)
    status = models.BooleanField(default = False, null = True, blank = True)

    
    def __str__(self):
        return str(self.id)
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.flag == False:
                shipping = True
        return shipping



class Payment(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('complete', 'Complete')
    )
    MODE = (
        ('credit card', 'Credit card'),
        ('debit card', 'Debit card'),
        ('cash', 'Cash'),
        ('upi', 'UPI')
    )
    customer_id = models.ForeignKey(Buyer, null=True, on_delete = models.CASCADE)
    status = models.CharField(max_length = 10, choices = STATUS)
    payment_mode = models.CharField(max_length = 20, choices = MODE)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    @property
    def get_total(self):
        total = self.product.cost * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Buyer, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    address = models.CharField(max_length = 200, null = False)
    city = models.CharField(max_length = 200, null = False)
    state = models.CharField(max_length = 200, null = False)
    zipcode = models.CharField(max_length = 200, null = False)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.address

    
