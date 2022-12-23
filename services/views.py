from django.shortcuts import render

# Create your views here.
def service(request):
    return render(request, 'service.html')

def services(request):
    return render(request,'services.html')
