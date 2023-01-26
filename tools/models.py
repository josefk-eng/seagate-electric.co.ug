from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.
class Tool(models.Model):
    toolImage = models.ImageField(upload_to="img/tools")
    name = models.CharField(max_length=150)
    small_desc = models.CharField(max_length=1000, blank=True, null=True)
    big_desc = models.CharField(max_length=1500, blank=True, null=True)
    features = models.CharField(max_length=1500, blank=True, null=True)
    specification = models.CharField(max_length=15000, blank=True, null=True)

    class Meta:
        verbose_name = _("Tool")
        verbose_name_plural = _("Tools")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tool_detail", kwargs={"pk": self.pk})
