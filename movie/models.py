from django.db import models


class Movie(models.Model):

    name = models.CharField(max_length=150)
    year = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=50, choices=(
        ('Acc', 'Acción'),
        ('CicFic', 'Ciencia ficción'),
        ('Com', 'Comedia'),
        ('Dram', 'Drama'),
        ('Fan', 'Fantasía'),
        ('MelDram', 'Melodrama'),
        ('Mus', 'Musical'),
        ('Rom', 'Romance'),
        ('Susp', 'Suspenso'),
        ('Terr', 'Terror'),
        ('Doc', 'Documental'),
    ))
    director = models.CharField(max_length=150)
    staff = models.JSONField()
    country = models.CharField(max_length=100)
