from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from services.models import Service

# Create your views here.
def about(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    return render(request,'company.html', {"products":products,"tools":tools,"services":services})
