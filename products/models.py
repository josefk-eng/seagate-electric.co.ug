from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=20,decimal_places=2, default=0.0)
    rating = models.IntegerField(default=0)
    type = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img/products") #800 by 600

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

