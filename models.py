from django.db import models

# Create your models here.
class contactdb(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)

class registerdb(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    contact = models.IntegerField(null=True,blank=True)


class buydb(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    contact = models.IntegerField(null=True,blank=True)
    quantity =models.IntegerField(null=True,blank=True)
    price =models.IntegerField(null=True,blank=True)
    total=models.IntegerField(null=True,blank=True)



