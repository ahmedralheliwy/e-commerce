from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.name