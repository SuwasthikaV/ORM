from django.db import models
from django.contrib import admin
# Create your models here.
class Product(models.Model):
    Product_Name=models.CharField(max_length=100)
    Product_Id=models.IntegerField(primary_key=True)
    Manufacture_Date=models.DateField()
    Expire_Date=models.DateField()
    Weight=models.CharField(max_length=10)
    Stock=models.IntegerField()
    Price=models.FloatField()
class ProductAdmin(admin.ModelAdmin):
    list_display=["Product_Name","Product_Id","Manufacture_Date","Expire_Date","Weight","Stock","Price"]