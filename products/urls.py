from django.conf import settings
from django.conf.urls import include, url

from .views import ProductDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)', ProductDetailView.as_view(), name='product_detail')
]
