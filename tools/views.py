from django.shortcuts import render

# Create your views here.
def tools(request):
    return render(request,'tools.html')

def tool(request):
    return render(request,'tool.html')
