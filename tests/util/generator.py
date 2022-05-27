from datetime import date

from movie.models import Movie
from faker import Faker
import random

faker = Faker()


def __generate_staff() -> dict:
    actors = []
    for i in range(3):
        actor_name = faker.name()
        actors.append(actor_name)
    return {'staff': actors}


def generate_movies(quantity: int) -> list:
    movies = []
    for i in range(quantity):
        a_movie = Movie()
        a_movie.name = faker.name()
        a_movie.year = random.randint(1900, date.today().year)
        a_movie.genre = random.choice(Movie.GENRES)[0]
        a_movie.director = faker.name()
        a_movie.staff = __generate_staff()
        a_movie.country = faker.country()
        movies.append(a_movie)
    return movies
