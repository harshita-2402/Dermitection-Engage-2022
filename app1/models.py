from django.db import models

# Create your models here.
class Disease(models.Model):
    id = models.IntegerField(primary_key = True)
    disease_name = models.CharField(max_length=100)
    symptoms = models.TextField()
    cure = models.TextField()