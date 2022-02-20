from django.shortcuts import render
from .models import Product


# Create your views here.
def get_product_details(request):
    products = Product.objects.all()
    context = {'product': products
    }
    return render(request, 'product/product_details.html', context)


