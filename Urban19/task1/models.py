from django.db import models


# Create your models here.
class Buyer(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    age = models.IntegerField()

    def __str__(self):
        return self.username


class Game(models.Model):
    title = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=5, decimal_places=1)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title

