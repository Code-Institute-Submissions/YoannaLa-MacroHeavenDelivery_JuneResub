from django.shortcuts import render
from .models import Product


# Create your views here.

def get_product(request):
    products = Product.objects.all()
    context = {'product': products}
    return render(request, 'product/product.html', context)


def product_add(request):
    return render(request, 'product/product_add.html')


def all_product(request):
    """
    A view to show all products
        """
    products = Product.objects.all()
    context = {'product': product,}
    return render(request, 'product/product.html', context)


def get_product_details(request, product_id):
    """ A view to show product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product,}
    return render(request, 'product/product_detail.html', context)

