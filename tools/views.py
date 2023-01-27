from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from services.models import Service
from contact.forms import EmailForm

# Create your views here.
def tools(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    return render(request,'tools.html', {"products":products,"tools":tools,"services":services})

def tool(request, name):
    products = Product.objects.all()
    tools = Tool.objects.all()
    tool = tools.get(name=name)
    services = Service.objects.all()
    e_form = EmailForm()
    return render(request,'tool.html', {"products":products,"tools":tools, "tool":tool,"services":services,"eform": e_form})