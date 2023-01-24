from django.contrib import admin
from . import models


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


# Register your models here.
admin.site.register(models.Service,ServiceAdmin)
admin.site.register(models.ServiceCard)
admin.site.register(models.Testimonial)
admin.site.register(models.MainDescription)
admin.site.register(models.ServiceImage)
admin.site.register(models.SideNotes)
