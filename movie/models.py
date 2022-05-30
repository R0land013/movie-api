from django.db import models


class Movie(models.Model):

    GENRES = (
        ('Acción', 'Acción'),
        ('Ciencia ficción', 'Ciencia ficción'),
        ('Comedia', 'Comedia'),
        ('Drama', 'Drama'),
        ('Fantasía', 'Fantasía'),
        ('Melodrama', 'Melodrama'),
        ('Musical', 'Musical'),
        ('Romance', 'Romance'),
        ('Suspenso', 'Suspenso'),
        ('Terror', 'Terror'),
        ('Documental', 'Documental'),
    )

    name = models.CharField(max_length=150)
    year = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=50, choices=GENRES)
    director = models.CharField(max_length=150)
    staff = models.JSONField()
    country = models.CharField(max_length=100)
