from django.db import models

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    street_address = models.CharField(max_length=1000)
    city = models.CharField(max_length=255)
    postcode = models.BigIntegerField()
    phone_number = models.BigIntegerField()
    email = models.EmailField()
    additional_info = models.TextField()