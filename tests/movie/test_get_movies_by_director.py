from django.test import TestCase
from rest_framework.status import HTTP_400_BAD_REQUEST

from movie.serializers import MovieSerializer
from tests.util.generator import generate_movies
from tests.util.helpers import delete_all_movies_from_database, save_movies_into_database, get_data_from_GET_request, \
    get_status_code_from_GET_request


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

        response_data = get_data_from_GET_request('/movie/director/',
                                                  {'director': 'Juan Carlos Tabío'})

        movie_serializer = MovieSerializer(data=[m1, m3], many=True)
        movie_serializer.is_valid()
        self.assertEqual(movie_serializer.data, response_data)

    def test_it_returns_status_BAD_REQUEST_400(self):
        movies = generate_movies(3)
        m1, m2, m3 = movies
        m1.director = 'Juan Carlos Tabío'
        m2.director = 'Steven Spielberg'
        m3.director = 'Juan Carlos Tabío'
        save_movies_into_database(movies)

        response_status = get_status_code_from_GET_request('/movie/director/',
                                                           {'direct': 'Juan Carlos Tabío'})

        self.assertEqual(response_status, HTTP_400_BAD_REQUEST)
