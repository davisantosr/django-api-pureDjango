from django.urls import path

#Because we're using media files, we need set this to tell the developer server about the files =>
from django.conf.urls.static import static
from django.conf import settings

from .views import ProductDetailView, ProductListView

urlpatterns = [
  path("", ProductListView.as_view(), name='product-list'),
  path("products/<int:pk>/", ProductDetailView.as_view(), name='product-detail')
]