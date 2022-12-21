from django.db import models

# Create your models here.

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
    description = models.TextField(max_length=1000000)
    category = models.ForeignKey (Category, related_name ='categorie', on_delete = models.CASCADE)
    image = models.CharField(max_length=500000)
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added',]
    def __str__(self):
        return self.title