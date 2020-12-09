from django.db import models

class Funds(models.Model):
    url = models.TextField(unique=True)
    name = models.TextField(unique=True) 
    aum = models.FloatField()
    snapshot = models.TextField()
    portfolio = models.TextField()

    def __str__(self):
        return self.name
