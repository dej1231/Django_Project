from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 120)
    description = models.TextField()
    quantity = models.DecimalField(decimal_places=2, max_digits=10000)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    is_available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return 


