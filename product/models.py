from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)


    def __str__(self):
        return str(self.name)

