from django.db import models
from django.contrib import admin
class Product(models.Model):
    Product_Name=models.CharField(max_length=100)
    Product_Id=models.IntegerField(primary_key=True)
    Country_of_Manufacture=models.CharField(max_length=100)
    Date_of_Manfacture=models.DateField()
    Price=models.FloatField()
    Company_Contact_Number=models.IntegerField()
    Email=models.EmailField()
class ProductAdmin(admin.ModelAdmin):
    list_display=["Product_Name","Product_Id","Country_of_Manufacture","Price","Company_Contact_Number","Email"]
