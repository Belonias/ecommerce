from django.shortcuts import render
from django.views.generic.detail import DetailView

# Create your views here.
from .models import Product

# cbv
class ProductDetailView(DetailView):
    model = Product


def product_detail_view(request, id):
    # we get the instance of product based on id
    product_instance = Product.objects.get(id=id)
    context = {
        'object': product_instance
    }
    template = 'products/product_detail.html'
    return render(request, template, context)
