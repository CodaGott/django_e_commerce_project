from django.shortcuts import render

from product.product_form import Product_form


def product_page(request):

    form = Product_form
    context = {'form': form}

    return render(request, 'product/product_page.html', context)


def create_product(request):
    form = Product_form
    context = {'form': form}
    return render(request, 'product/create_product_page.html', context)


def product_details(request):
    return render(request, 'product/product_detail.html')
