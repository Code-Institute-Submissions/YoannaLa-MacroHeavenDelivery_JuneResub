from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.views import generic, View
from django.http import HttpResponseRedirect


# Create your views here.
def get_product_details(request):
    return render(request, 'product/product_details.html')

def all_products(request):
    """
A view to show all products
        """
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    return render(request, 'products/products.html',)
    
