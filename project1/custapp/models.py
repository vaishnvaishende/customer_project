from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=50)
    phoneno = PhoneNumberField()
    address = models.CharField(max_length=50)

