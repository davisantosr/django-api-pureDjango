from django.urls import path

#Because we're using media files, we need set this to tell the developer server about the files =>
from django.conf.urls.static import static
from django.conf import settings

# from .views import ProductDetailView, ProductListView
from .views import (
  manufacturer_detail, manufacturer_list, product_list, product_detail, )

urlpatterns = [
  path("products/", product_list, name='product-list'),
  path("products/<int:pk>/", product_detail, name='product-detail'),

  path("manufacturers/", manufacturer_list, name='manafacturers-list'),
  path("manufacturers/<int:pk>/", manufacturer_detail, name='manafacturers-list'),



]