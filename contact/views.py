from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from services.models import Service

# Create your views here.
def contact(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()[1]
    return render(request,"contact.html", {"products":products,"tools":tools,"services":services})
