from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic import View
from .models import ProductCategory, Product

# Create your views here.
def index(request):
    context = {}
    context["products"] = {}
    
    productCategories = ProductCategory.objects.all()

    for productCategory in productCategories.iterator():
        context["products"][productCategory.title] = Product.objects.filter(category=productCategory)
    return render(request, 'pos.html', context)

