from django.urls import path
from . import views

urlpatterns = [
    path('service/<int:id>', views.service, name="service"),
    path('',views.services, name='services')
]
