from django.db import models

# Create your models here.
class ShopIT(models.Model):
    name = models.CharField(max_length=255)
    price =  models.DecimalField(max_length=10, decimal_places=4,max_digits=13)
    quantity = models.PositiveIntegerField()
    img= models.CharField(max_length=2083)
    
    
