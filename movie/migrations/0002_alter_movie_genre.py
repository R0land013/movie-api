# Generated by Django 4.0.4 on 2022-06-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Acción', 'Acción'), ('Ciencia ficción', 'Ciencia ficción'), ('Comedia', 'Comedia'), ('Drama', 'Drama'), ('Fantasía', 'Fantasía'), ('Melodrama', 'Melodrama'), ('Musical', 'Musical'), ('Romance', 'Romance'), ('Suspenso', 'Suspenso'), ('Terror', 'Terror'), ('Documental', 'Documental')], max_length=50),
        ),
    ]