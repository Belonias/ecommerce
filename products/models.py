from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save

# Create your models here.
class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)


class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)
    # created a new manager to customize the queryset
	def all(self, *args, **kwargs):
		return self.get_queryset().active()

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    #slug
    price = models.DecimalField(decimal_places=2, max_digits=100)
    #inventory
    active = models.BooleanField(default=True)
    objects = ProductManager()

    def __str__(self):
        return self.title

def get_absolute_url(self):
		return reverse("product_detail", kwargs={"pk": self.pk})


class Variation(models.Model):
	product = models.ForeignKey(Product)
	title = models.CharField(max_length=120)
	price = models.DecimalField(decimal_places=2, max_digits=100)
	sale_price = models.DecimalField(decimal_places=2 , max_digits=100, null=True, blank=True)
	active = models.BooleanField(default=True)
	inventory = models.IntegerField(null=True, blank=True) # unlimited amount

	def __str__(self):
		return self.title

	def get_price(self):
		if self.sale_price is not None:
			return self.sale_price
		else:
			return self.price

	def get_absolute_url(self):
		return self.product.get_absolute_url()

def product_post_saved_receiver(sender, instance, created, *args, **kwargs):
	product = instance
	variations = product.variation_set.all()
	if variations.count() == 0:
		new_var = Variation()
		new_var.product = product
		new_var.title = 'Default'
		new_var.price = product.price
		new_var.save()

post_save.connect(product_post_saved_receiver, Product)
