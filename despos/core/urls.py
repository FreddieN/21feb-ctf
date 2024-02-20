from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receipt', views.receipt, name='receipt'),
    path('void', views.void, name='receipt'),
    path('checkout', views.checkout, name='receipt'),
    path('addProduct/<int:product_id>', views.addProduct, name='receipt')
] 