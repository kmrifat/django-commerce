from django.db import models


# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'customers'


class CustomerAddress(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address_line = models.CharField(max_length=255)
    additional_address_line = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'customer_address'
