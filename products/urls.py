from django.urls import path

#Because we're using media files, we need set this to tell the developer server about the files =>
from django.conf.urls.static import static
from django.conf import settings

# from .views import ProductDetailView, ProductListView
from .views import product_list, product_detail

urlpatterns = [
  path("products/", product_list, name='product-list'),
  path("products/<int:pk>/", product_detail, name='product-detail'),

]