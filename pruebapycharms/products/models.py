from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_length=9, decimal_places=2, max_digits=10)
    quantity = models.IntegerField()

    def __str__(self):
        return self.description
