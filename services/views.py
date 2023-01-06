from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from .models import Service, ServiceCard, MainDescription, Testimonial, SlidingImage


# Create your views here.
def service(request, id):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()[0]
    service = Service.objects.get(id=id)
    cards = ServiceCard.objects.filter(service=id)
    mainDesc = MainDescription.objects.all()[0]
    mainDesc1 = MainDescription.objects.all()[1]
    testimonials = Testimonial.objects.all()
    slidingImages = SlidingImage.objects.filter(description=mainDesc.id)
    return render(request, 'service.html', {"products":products,"tools":tools,"service":service,"cards":cards,"services":services,"desc":mainDesc,"desc1":mainDesc1,"tests":testimonials,"sliders":slidingImages})

def services(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    return render(request,'services.html', {"products":products,"tools":tools})
