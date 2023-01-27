from django.shortcuts import render
from products.models import Product
from tools.models import Tool
from .models import Service, ServiceCard, MainDescription, Testimonial, ServiceImage, SideNotes
from contact.forms import EmailForm


# Create your views here.
def service(request, id):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    service = Service.objects.get(id=id)
    cards = ServiceCard.objects.filter(service=id)
    mainDesc = MainDescription.objects.all()[0]
    mainDesc1 = MainDescription.objects.all()[1]
    testimonials = Testimonial.objects.all()
    slidingImages = ServiceImage.objects.filter(service=id)
    notes = SideNotes.objects.filter(service=id)
    e_form = EmailForm()
    return render(request, 'ServicePage.html', {"products":products,"tools":tools,"service":service,"cards":cards,"services":services,"desc":mainDesc,"desc1":mainDesc1,"tests":testimonials,"sliders":slidingImages,"sidenotes":notes,"eform": e_form})

def services(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    images = ServiceImage.objects.all()
    notes = SideNotes.objects.all()
    return render(request,'ServicePage.html', {"products":products,"tools":tools,"services":services,"tests":testimonials,"images":images,"sidenotes":notes})


#http://127.0.0.1:5000/services/service/2