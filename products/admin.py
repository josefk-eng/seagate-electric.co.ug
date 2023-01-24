from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


# Register your models here.
admin.site.register(models.Product, ProductAdmin)
