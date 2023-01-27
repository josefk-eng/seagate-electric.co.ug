from django.shortcuts import render
from .models import Product
from tools.models import Tool
from services.models import Service
from contact.forms import EmailForm

# Create your views here.
def products(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    return render(request,'products.html',{"products":products,"tools":tools,"services":services})

def product(request, id):
    products = Product.objects.all()
    tools = Tool.objects.all()
    product = products.get(id=id)
    services = Service.objects.all()
    e_form = EmailForm()
    return render(request,'product.html', {'product':product,"products":products,"tools":tools,"services":services,"eform": e_form})