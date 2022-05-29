from movie.models import Movie


def save_movies_into_database(movies: list):
    for a_movie in movies:
        a_movie.save()


def delete_all_movies_from_database():
    movies = Movie.objects.all()
    for a_movie in movies:
        a_movie.delete()
