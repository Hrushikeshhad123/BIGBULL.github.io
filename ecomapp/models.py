from django.db import models
from django.contrib.auth.models import User                

# Create your models here.
CATEGORY_CHOICES =(
    ('TS','T-SHIRTS'),
    ('HO','HOODIES'),
    ('BO','BOOKS'),
    ('JO','JOURNAL'),
    ('PO','PROFIT DIARY'),
    ('GA','GAMES'),
)





class Products (models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.CharField(max_length=100)
    discounted_price = models.CharField(max_length=100)
    desc = models.TextField()
    comp = models.TextField(default = "")
    prodapp = models.TextField(default = " ")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    prod_img = models.ImageField(upload_to = 'product')

    def __str__(self):
        return self.title




class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default = 0)
    zipcode = models.IntegerField()


    def __str__(self):
        return self.name

class Cart(models.Model):
  
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price