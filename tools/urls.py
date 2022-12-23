from django.urls import path
from . import views

urlpatterns = [
    path('',views.tools,name="tools"),
    path('tool',views.tool,name='tool')
]
