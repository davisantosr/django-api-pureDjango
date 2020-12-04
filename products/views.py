from django.http import JsonResponse

from .models import Manufacturer, Product

def product_list(request):
  products = Product.objects.all() #[:30]slice avaliable
  data = {"products": list(products.values())}  #values("pk", "name")
  response = JsonResponse(data)

  return response

def product_detail(request, pk):
  try:
    product = Product.objects.get(pk=pk)
    data = { 
      "product": {
        "name": product.name,
        "manufacturer": product.manufacturer.name,
        "description": product.description,
        "photo": product.photo.url,
        "price": product.price,
        "shipping_cost": product.shipping_cost,
        "quantity": product.quantity,  
    }}

    response = JsonResponse(data)
  except Product.DoesNotExist:
    response = JsonResponse({
      "error": {
        "code": 404,
        "message": "Product not found"
      }
    }, status=404)
  return response

def manufacturer_list(request):
  manufacturers = Manufacturer.objects.filter(active=True)
  data = {"manufacturers": list(manufacturers.values())}
  response = JsonResponse(data)
  return response


def manufacturer_detail(request, pk):
  try:
    manufacturer = Manufacturer.objects.get(pk=pk)
    manufacturer_products = manufacturer.products.all()
    data = { 
      "Manufacturer": {
        "name": manufacturer.name, 
        "location": manufacturer.location,
        "active": manufacturer.active,
        "products": list(manufacturer_products.values())
    }}
    response = JsonResponse(data)

  except Product.DoesNotExist:
    response = JsonResponse({
      "error": {
        "code": 404,
        "message": "Manufacturer not found"
      }
    }, status=404)
  return response

  