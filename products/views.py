from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.db.models import Q
# Create your views here.
from .models import Product

# cbv
class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    # overide the defaul method
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            qs = self.model.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
            )
            try:
                qs2 = self.model.objects.filter(
                    Q(price=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs

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
