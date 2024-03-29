from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.views.generic import View
from .models import ProductCategory, Product, Cart, CartEntry
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    context = {}
    context["products"] = {}

    cart, created = Cart.objects.get_or_create(user=request.user)
    context["cart"] = cart
    
    productCategories = ProductCategory.objects.all()

    context["total"] = sum(entry.item.price for entry in cart.entries.all())

    for productCategory in productCategories.iterator():
        context["products"][productCategory.title] = Product.objects.filter(category=productCategory)
    return render(request, 'pos.html', context)
@login_required
def receipt(request):
    context = {}
    
    return render(request, 'receipt.html', context)
@login_required
def void(request):
    context = {}
    
    return redirect('/')
@login_required
def checkout(request):
    
    return redirect('/')
@login_required
def addProduct(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    itemToAdd = Product.objects.get(pk=product_id)
    cartEntryMade = CartEntry.objects.create(item=itemToAdd)
    cart.entries.add(cartEntryMade)
    return redirect('/')
