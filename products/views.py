from django.shortcuts import render
from .models import Product
from tools.models import Tool
from services.models import Service

# Create your views here.
def products(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()[1]
    return render(request,'products.html',{"products":products,"tools":tools,"services":services})

def product(request, id):
    products = Product.objects.all()
    tools = Tool.objects.all()
    product = products.get(id=id)
    services = Service.objects.all()[1]
    return render(request,'product.html', {'product':product,"products":products,"tools":tools,"services":services})