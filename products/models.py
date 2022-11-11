from django.db import models
from django.conf import settings

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=250, blank=True)
    model_name = models.CharField(max_length=250, blank=True)
    color = models.CharField(max_length=250, blank=True)
    fixed_price = models.IntegerField()
    special_price = models.IntegerField()
    os = models.CharField(max_length=250, blank=True)
    processor = models.CharField(max_length=250, blank=True)
    security_function = models.CharField(max_length=250, blank=True)
    input_device = models.CharField(max_length=250, blank=True)
    network = models.CharField(max_length=250, blank=True)
    multimedia = models.CharField(max_length=250, blank=True)
    power_consumption = models.IntegerField()
    rated_voltage = models.IntegerField()


class Graphics(models.Model):
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    integrated_graphics = models.CharField(max_length=250, blank=True)
    external_graphics = models.CharField(max_length=250, blank=True)


class ProductComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    content = models.TextField()
