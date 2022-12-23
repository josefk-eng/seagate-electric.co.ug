from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to="img/sliders")
    header = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Sliders")

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse("Slider_detail", kwargs={"pk": self.pk})
    
    
class WelcomingNote(models.Model):
    sideImage = models.ImageField(upload_to="img/abt")
    header = models.CharField(max_length=30)
    subheader = models.CharField(max_length=100)
    descriptive_text = models.CharField(max_length=500)
    bullet_list = models.CharField(max_length=500)
    

    class Meta:
        verbose_name = _("WelcomingNote")
        verbose_name_plural = _("WelcomingNotes")

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse("WelcomingNote_detail", kwargs={"pk": self.pk})
    
    
class WhyChooseUS(models.Model):
    header = models.CharField(max_length=100)
    subHeader = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = _("WhyChooseUS")
        verbose_name_plural = _("WhyChooseUSs")

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse("WhyChooseUS_detail", kwargs={"pk": self.pk})
    
class PortFolio(models.Model):
    tab_text = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = _("PortFolio")
        verbose_name_plural = _("PortFolios")

    def __str__(self):
        return self.tab_text

    def get_absolute_url(self):
        return reverse("PortFolio_detail", kwargs={"pk": self.pk})
    
    
class PortfolioImages(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/portfolio")
    portfolio = models.ForeignKey(PortFolio, verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("PortfolioImages")
        verbose_name_plural = _("PortfolioImagess")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("PortfolioImages_detail", kwargs={"pk": self.pk})
    
    
class ClientImages(models.Model):
    client = models.CharField(max_length=100, default="")
    client_image = models.ImageField(upload_to="img/clients")

    class Meta:
        verbose_name = _("ClientImages")
        verbose_name_plural = _("ClientImagess")

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse("ClientImages_detail", kwargs={"pk": self.pk})







