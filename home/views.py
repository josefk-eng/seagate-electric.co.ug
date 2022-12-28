from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from .models import Slider
from services.models import Service

# Create your views here.
def home(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    sliders = Slider.objects.all()
    return render(request, 'home.html', {"products":products, "tools":tools,"sliders":sliders,"services":services})
