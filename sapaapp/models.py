from django.db import models
from datetime import datetime
import os
# Create your models here.


class Querie(models.Model):
    sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=30)
    Message = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    sno = models.AutoField(primary_key=True)
    Active = models.BooleanField(default=True)
    Image = models.ImageField(upload_to='Products')
    Product_Name = models.CharField(max_length=80)
    Minimum_Quantity = models.CharField(max_length=5000, null=True, blank=True)
    Price = models.CharField(max_length=5000, null=True, blank=True)
    Price_Range = models.CharField(max_length=5000, null=True, blank=True)
    Features = models.TextField(max_length=5000, null=True, blank=True)
    Instructions = models.TextField(max_length=5000, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

