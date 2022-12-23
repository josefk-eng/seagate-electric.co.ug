from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.
class CompanyBanner(models.Model):

    banner = models.ImageField(upload_to="img/banners")

    class Meta:
        verbose_name = _("CompanyBanner")
        verbose_name_plural = _("CompanyBanners")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CompanyBanner_detail", kwargs={"pk": self.pk})
    
    
class AboutIntro(models.Model):

    header = models.CharField(max_length=100)
    subHeader = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    service_list = models.CharField(max_length=1000)
    footNote = models.CharField(max_length=1000)
    sideImage = models.ImageField(upload_to="img/abt")

    class Meta:
        verbose_name = _("AboutIntro")
        verbose_name_plural = _("AboutIntros")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("AboutIntro_detail", kwargs={"pk": self.pk})
    
    
class CompanyStatement(models.Model):

    icon = models.CharField(max_length=1000)
    header = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)

    class Meta:
        verbose_name = _("CompanyStatement")
        verbose_name_plural = _("CompanyStatements")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CompanyStatement_detail", kwargs={"pk": self.pk})

    



