from rest_framework.parsers import JSONParser
from movie.models import Movie
import json
from django.test import Client
import io


def save_movies_into_database(movies: list):
    for a_movie in movies:
        a_movie.save()


def delete_all_movies_from_database():
    movies = Movie.objects.all()
    for a_movie in movies:
        a_movie.delete()


def get_data_from_GET_request(url: str, data: dict):
    request_data = json.dumps(data)
    response = Client().generic('GET', url, request_data, 'application/json')
    stream = io.BytesIO(response.content)
    retrieved_data = JSONParser().parse(stream)
    return retrieved_data


def get_status_code_from_GET_request(url: str, data: dict):
    request_data = json.dumps(data)
    response = Client().generic('GET', url, request_data, 'application/json')
    return response.status_code
