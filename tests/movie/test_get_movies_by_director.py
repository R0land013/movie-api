from django.test import TestCase

from movie.serializers import MovieSerializer
from tests.util.generator import generate_movies
from tests.util.helpers import delete_all_movies_from_database, save_movies_into_database, get_request_using_json


class TestGetMoviesByDirector(TestCase):

    def setUp(self):
        delete_all_movies_from_database()

    def test_get_movies_by_director(self):
        movies = generate_movies(3)
        m1, m2, m3 = movies
        m1.director = 'Juan Carlos Tabío'
        m2.director = 'Steven Spielberg'
        m3.director = 'Juan Carlos Tabío'
        save_movies_into_database(movies)

        response_data = get_request_using_json('/movie/director/',
                                               {'director': 'Juan Carlos Tabío'})

        movie_serializer = MovieSerializer(data=[m1, m3], many=True)
        movie_serializer.is_valid()
        self.assertEqual(movie_serializer.data, response_data)