from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic.detail import DetailView

# Create your views here.
from .models import Product

# cbv
class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    # overide the defaul method
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

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
