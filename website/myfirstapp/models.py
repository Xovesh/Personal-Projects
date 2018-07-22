from django.db import models


# Create your models here.

class Pokemon(models.Model):
    number = models.CharField(max_length=5, default="00000")
    name = models.CharField(max_length=20)
    height = models.FloatField()
    weight = models.FloatField()
    gender = models.IntegerField()
    category = models.CharField(max_length=50)
    abilities = models.CharField(max_length=50)
    ptype = models.CharField(max_length=50)
    weakness = models.CharField(max_length=50)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    firstevolution = models.BooleanField()

    def __str__(self):
        return self.number + " " + self.name
