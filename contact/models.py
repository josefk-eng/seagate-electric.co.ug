from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.
class Contact(models.Model):

    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    mapAPI = models.CharField(max_length=1000)
    destinationEmail = models.EmailField(max_length=100)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})

