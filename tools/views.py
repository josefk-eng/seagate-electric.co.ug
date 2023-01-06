from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from services.models import Service

# Create your views here.
def tools(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()[1]
    return render(request,'tools.html', {"products":products,"tools":tools,"services":services})

def tool(request, id):
    products = Product.objects.all()
    tools = Tool.objects.all()
    tool = tools.get(id=id)
    services = Service.objects.all()[1]
    return render(request,'tool.html', {"products":products,"tools":tools, "tool":tool,"services":services})