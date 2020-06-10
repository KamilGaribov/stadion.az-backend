from django.db import models
from django.contrib.auth.models import User


floor_choices = [('ot', 'ot'),('rezin', 'rezin'),('xalca', 'xalca')]
size_choices = [('5vs5', '5vs5'), ('6vs6', '6vs6'), ('7vs7', '7vs7'), ('11vs11', '11vs11')]
days = [('mon', 'mon'),('tue', 'tue'),('wed', 'wed'),('thu', 'thu'),('fri', 'fri'),('sat', 'sat'), ('sun', 'sun')]
stars = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class Stadion(models.Model):
    name = models.CharField(max_length=63)
    city = models.CharField(max_length=63)
    district = models.CharField(max_length=63, null=True, blank=True)
    metro = models.CharField(max_length=63, null=True, blank=True)
    adress = models.CharField(max_length=63, null=True, blank=True)
    floor = models.CharField(max_length=7, choices=floor_choices)
    size = models.CharField(max_length=7, choices=size_choices)
    price = models.IntegerField()
    cover = models.BooleanField(default=False)
    cafe = models.BooleanField(default=False)
    park = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    ordered = models.PositiveIntegerField(default=0)
    star = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Stadion"
        verbose_name_plural = "Stadionlar"
    
    def __str__(self):
        return self.name


class Hour(models.Model):
    stadion = models.ForeignKey(Stadion, on_delete=models.CASCADE)
    day = models.CharField(max_length=7, choices=days)
    nine = models.BooleanField(default=False)
    ten = models.BooleanField(default=False)
    eleven = models.BooleanField(default=False)
    twelve = models.BooleanField(default=False)

    def __str__ (self):
        return self.stadion.name + " - " + self.day


class StadionImage(models.Model):
    stadion = models.ForeignKey(Stadion, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stadion/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.stadion.name


class StadionFeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadion = models.ForeignKey(Stadion, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=stars)
    comment = models.TextField(null=True, blank=True)
    def __str__ (self):
        return self.stadion.name


class Team(models.Model):
    name = models.CharField(max_length=63)
    bio = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=63)
    played = models.PositiveIntegerField(default=0)
    win = models.PositiveIntegerField(default=0)
    draw = models.PositiveIntegerField(default=0)
    lose = models.PositiveIntegerField(default=0)
    player = models.ManyToManyField(User)
    def __str__ (self):
        return self.name