from django.urls import path
from . import views

urlpatterns = [
    path('',views.tools,name="tools"),
    path('tool/<int:id>',views.tool,name='tool')
]