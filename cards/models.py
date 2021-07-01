from django.db import models
# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=50)


class Card(models.Model):
    collection = models.ForeignKey(Collection, blank=True, null=True, on_delete=models.CASCADE)
    term = models.CharField(max_length=50)
    definition = models.CharField(max_length=250)