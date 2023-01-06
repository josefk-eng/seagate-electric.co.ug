from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Service)
admin.site.register(models.ServiceCard)
admin.site.register(models.Testimonial)
admin.site.register(models.MainDescription)
admin.site.register(models.SlidingImage)