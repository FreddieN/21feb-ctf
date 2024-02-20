from django.db import models

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