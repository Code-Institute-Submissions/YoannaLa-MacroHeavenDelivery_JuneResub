from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=200)
    product_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_product_name(self):
        return self.product_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    image = CloudinaryField('image',)
    description = models.TextField()
    size = models.CharField(max_length=200, null=True, blank=True,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
   

    def __str__(self):
        return str(self.name)
