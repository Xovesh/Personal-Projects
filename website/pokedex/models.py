from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=40)
    height = models.FloatField()
    weigth = models.FloatField()
    gender = models.CharField(max_length=20)
    category = models.CharField(max_length=200)
    abilities = models.CharField(max_length=200)
    ptype = models.CharField(max_length=200)
    weakness = models.CharField(max_length=200)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    firstevolution = models.BooleanField()

    def __str__(self):
        return "Number: %i, Name: %s" % (self.pk, self.name)
