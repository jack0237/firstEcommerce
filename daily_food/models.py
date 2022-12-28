from django.db import models
from django.conf import settings



class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added',]

    def __str__(self):
        return self.name
           
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(max_length=20)
    stock = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=1000000)
    category = models.ForeignKey (Category, related_name ='categorie', on_delete = models.CASCADE)
    image = models.CharField(max_length=500000)
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added',]

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):

        return f"{self.product.name} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order) 
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username         