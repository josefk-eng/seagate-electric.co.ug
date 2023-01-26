from django.urls import path
from . import views

urlpatterns = [
    path('',views.tools,name="tools"),
    path('<name>',views.tool,name='tool')
]