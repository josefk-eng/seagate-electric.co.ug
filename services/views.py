from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from .models import Service, ServiceCard


# Create your views here.
def service(request, id):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    service = services.get(id=id)
    cards = ServiceCard.objects.filter(service=id)
    return render(request, 'service.html', {"products":products,"tools":tools,"service":service,"cards":cards,"services":services})

def services(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    return render(request,'services.html', {"products":products,"tools":tools})
