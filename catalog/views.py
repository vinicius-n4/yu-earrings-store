from django.shortcuts import render

from .models import Product


def product_list(request):
    products = (
        Product.objects
        .order_by('-available', 'name')
        .prefetch_related('images')
    )
    return render(request, 'catalog/product_list.html', {'products': products})
