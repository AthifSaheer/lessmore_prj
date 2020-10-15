from django.db import models

# Create your models here.

class laptop(models.Model):
    image = models.ImageField(upload_to='pics')
    brand = models.CharField(max_length=50)
    offer_upto = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    sub_brand = models.CharField(max_length=50)
    add_to_cart = models.BooleanField(default=False)
    buy_now = models.BooleanField(default=False)
    out_of_stock = models.BooleanField(default=False)
    notify_me = models.BooleanField(default=False)