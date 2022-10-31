from django.db import models

# Create your models here.

class selectionModel(models.Model):
    animal=models.CharField(max_length=50,null=True,blank=True)
    breed=models.CharField(max_length=100,null=True,blank=True)


class ResultsModel(models.Model):
    animal=models.CharField(max_length=50,null=True,blank=True)
    breed=models.CharField(max_length=100,null=True,blank=True)
    created_date=models.CharField(max_length=100,null=True,blank=True)
