from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from .models import Slider, WhyChooseUS, ClientImages, PortFolio, PortfolioImages
from services.models import Service
from contact.forms import EmailForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    sliders = Slider.objects.all()
    reasons = WhyChooseUS.objects.all()
    clients = ClientImages.objects.all()
    portfolios = PortFolio.objects.all()
    p_images = PortfolioImages.objects.all()
    e_form = EmailForm()
    return render(request, 'home.html', {"products":products,
                                         "tools":tools,
                                         "sliders":sliders,
                                         "services":services,
                                         "reasons":reasons,
                                         "clients":clients,
                                         "portfolios":portfolios,
                                         "p_images":p_images,"eform": e_form
                                         })
