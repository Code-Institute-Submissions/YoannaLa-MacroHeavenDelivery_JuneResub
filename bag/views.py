from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from product.models import Product


def view_bag(request):
    """ A view to return the bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated "{product.name}" quantity in your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added "{product.name}" to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """ Edit products in bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated "{product.name}" quantity in your bag')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed "{product.name}" from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove product from bag """

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed "{product.name}" from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing "{product.name}: {e}"')
        return HttpResponse(status=500)