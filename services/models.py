from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.
class Service(models.Model):

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=1000)
    banner = models.ImageField(upload_to="img/services")
    description = models.CharField(max_length=1500)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})
    
    
class ServiceCard(models.Model):

    service = models.ForeignKey(Service, verbose_name=_(""), on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    sideImage = models.ImageField(upload_to="img/serviceCards")
    description = models.CharField(max_length=2500)


    class Meta:
        verbose_name = _("ServiceCard")
        verbose_name_plural = _("ServiceCards")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ServiceCard_detail", kwargs={"pk": self.pk})
    

class Testimonial(models.Model):

    comment = models.CharField(max_length=2000)
    owner = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse("Testimonial_detail", kwargs={"pk": self.pk})


