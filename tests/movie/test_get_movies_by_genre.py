from django.test import TestCase

from movie.serializers import MovieSerializer
from tests.util.generator import generate_movies
from tests.util.helpers import delete_all_movies_from_database, save_movies_into_database, get_request_using_json


class TestGetMoviesByGenre(TestCase):

    def setUp(self):
        delete_all_movies_from_database()

    def test_get_movies_by_genre(self):
        movies = generate_movies(3)
        m1, m2, m3 = movies
        m1.genre = 'Drama'
        m2.genre = 'Terror'
        m3.genre = 'Drama'
        save_movies_into_database(movies)

        response_data = get_request_using_json('/movie/genre/', {'genre': 'Drama'})

        movie_serializer = MovieSerializer(data=[m1, m3], many=True)
        movie_serializer.is_valid()
        self.assertEqual(movie_serializer.data, response_data)
