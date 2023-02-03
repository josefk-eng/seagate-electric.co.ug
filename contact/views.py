from django.shortcuts import render, redirect
from products.models import Product
from tools.models import Tool
from services.models import Service
from .forms import ContactMessageForm, EmailForm
from django.contrib import messages
from SeaGateProject.emailConfigs import sendMail


# Create your views here.
def contact(request):
    products = Product.objects.all()
    tools = Tool.objects.all()
    services = Service.objects.all()
    form = ContactMessageForm()
    e_form = EmailForm()
    return render(request, "contact.html",
                  {"products": products, "tools": tools, "services": services, "form": form, "eform": e_form})


def feedback(request):
    if request.method == 'POST':
        contactForm = ContactMessageForm(data=request.POST)
        if contactForm.is_valid():
            contactForm.save()
            title = request.POST['name']
            if title is None:
                title = request.POST['email']
            sendMail(
                subject=f"{request.POST['subject']} from {title}",
                message=request.POST['message'],
                rcpt_list=["kigozijosefed1993@gmail.com", ]
            )
            messages.success(request, "Your message has been sent successfully. Thank You")
            return redirect('contact')
        else:
            messages.error(request, "Could not send your message please try again")
            return redirect('contact')

    else:
        print("Nothing is done")
        return redirect('contact')


def useremail(request, current):
    if request.method == 'POST':
        emailForm = EmailForm(data=request.POST)
        if emailForm.is_valid():
            emailForm.save()
            return redirect('Home')
        else:
            return redirect('Home')
    else:
        return redirect('Home')
