from django.shortcuts import render, redirect
from products.models import Product
from tools.models import Tool
from services.models import Service
from .forms import ContactMessageForm
from django.contrib import messages

# Create your views here.
def contact(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    form = ContactMessageForm()
    return render(request,"contact.html", {"products":products,"tools":tools,"services":services,"form":form})


def feedback(request):
    if request.method == 'POST':
        contactForm = ContactMessageForm(data=request.POST)
        print("reached here")
        if contactForm.is_valid():
            contactForm.save()
            messages.success(request, "Your message has been sent successfully. Thank You")
            return redirect('contact')
        else:
            messages.error(request,"Could not send your message please try again")
            return redirect('contact')

    else:
        print("Nothing is done")
        return redirect('contact')
