from django.test import TestCase
from django.test import Client
from rest_framework.test import APITestCase
from movie.serializers import MovieSerializer
from tests.util.generator import generate_movies
from tests.util.helpers import delete_all_movies_from_database, save_movies_into_database, GET_request_using_json
import io
from rest_framework.parsers import JSONParser
import json


class TestGetMoviesByCountry(APITestCase):

    def setUp(self):
        delete_all_movies_from_database()

    def test_movies_are_got_by_country(self):
        movies = generate_movies(3)
        m1, m2, m3 = movies
        m1.country = 'Cuba'
        m2.country = 'France'
        m3.country = 'Cuba'
        save_movies_into_database(movies)

        response_data = GET_request_using_json('/movie/by_country/', {'country': 'Cuba'})

        movie_serializer = MovieSerializer(data=[m1, m3], many=True)
        movie_serializer.is_valid()
        self.assertEqual(response_data, movie_serializer.data)
