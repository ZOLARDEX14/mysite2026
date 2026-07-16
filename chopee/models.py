from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return self.name
