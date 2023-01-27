from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from services.models import Service
from .models import AboutIntro
from contact.forms import EmailForm

# Create your views here.
def about(request, id):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    about = AboutIntro.objects.first
    e_form = EmailForm()
    return render(request,'company.html', {"products":products,"tools":tools,"services":services, "about":about,"eform": e_form})
