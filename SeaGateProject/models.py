from django.db import models
from django.urls import reverse
class Service(models.Model):
    id = models.IntegerField()
    description = models.CharField(max_length=50)    

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})
