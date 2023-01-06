from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from .models import Slider, WhyChooseUS, ClientImages
from services.models import Service

# Create your views here.
def home(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()[1]
    sliders = Slider.objects.all()
    reasons = WhyChooseUS.objects.all()
    clients = ClientImages.objects.all()
    return render(request, 'home.html', {"products":products, "tools":tools,"sliders":sliders,"services":services,"reasons":reasons,"clients":clients})
