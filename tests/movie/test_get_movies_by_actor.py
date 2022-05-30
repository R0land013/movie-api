from django.test import TestCase

from movie.serializers import MovieSerializer
from tests.util.generator import generate_movies
from tests.util.helpers import delete_all_movies_from_database, save_movies_into_database, GET_request_using_json


class TestGetMoviesByActor(TestCase):

    def setUp(self):
        delete_all_movies_from_database()

    def test_get_movies_by_actor(self):
        movies = generate_movies(3)
        m1, m2, m3 = movies
        m1.staff = {'staff': ['Tom Hanks', 'Jorge Perrugorría']}
        m2.staff = {'staff': 'Omar Sy'}
        m3.staff = {'staff': ['Tom Hanks', 'Jorge Perrugorría']}
        save_movies_into_database(movies)

        response_data = GET_request_using_json('/movie/by_actor/', {'actor': 'Tom Hanks'})

        movie_serializer = MovieSerializer(data=[m1, m3], many=True)
        movie_serializer.is_valid()
        self.assertEqual(response_data, movie_serializer.data)
