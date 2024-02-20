from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.pk}"
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=1)
    thumbnail = models.ImageField()
    category = models.ManyToManyField(ProductCategory)
    def __str__(self):
        return f"{self.title} - {self.pk}"
    
class CartEntry(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item} - {self.pk}"
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entries = models.ManyToManyField(CartEntry)
    def __str__(self):
        return f"{self.user} - {self.pk}"