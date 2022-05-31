from rest_framework.test import APITestCase
from movie.serializers import MovieSerializer
from tests.util.generator import generate_movies
from tests.util.helpers import delete_all_movies_from_database, save_movies_into_database, get_data_from_GET_request, \
    get_status_code_from_GET_request
from rest_framework.status import HTTP_400_BAD_REQUEST


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

        response_data = get_data_from_GET_request('/movie/country/', {'country': 'Cuba'})

        movie_serializer = MovieSerializer(data=[m1, m3], many=True)
        movie_serializer.is_valid()
        self.assertEqual(response_data, movie_serializer.data)

    def test_it_returns_status_BAD_REQUEST_400(self):
        movies = generate_movies(3)
        m1, m2, m3 = movies
        m1.country = 'Cuba'
        m2.country = 'France'
        m3.country = 'Cuba'
        save_movies_into_database(movies)

        response_status = get_status_code_from_GET_request('/movie/country/',
                                                           {'countries': 'Cuba'})

        self.assertEqual(response_status, HTTP_400_BAD_REQUEST)
