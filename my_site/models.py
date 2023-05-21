from django.db import models


# Create your models here.
class Count(models.Model):
    id = models.BigAutoField(primary_key=True)
    counter = models.IntegerField(default=0)
    lastModifie = models.CharField(default="none", max_length=150)
