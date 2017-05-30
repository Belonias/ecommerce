from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    #slug
    price = models.DecimalField(decimal_places=2 , max_digits=100)
    #inventory
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

def get_absolute_url(self):
		return reverse("product_detail", kwargs={"pk": self.pk})
