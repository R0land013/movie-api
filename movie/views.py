from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from movie.models import Movie
from movie.serializers import MovieSerializer
from rest_framework.decorators import action
from rest_framework.status import HTTP_400_BAD_REQUEST


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'], url_path='by_country')
    def get_movies_by_country(self, request):
        if 'country' not in request.data:
            return Response(status=HTTP_400_BAD_REQUEST)

        country = request.data['country']

        movies_by_country = self.queryset.filter(country=country)
        serializer = MovieSerializer(data=movies_by_country, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'], url_path='by_actor')
    def get_movies_by_actor(self, request):

        if 'actor' not in request.data:
            return Response(status=HTTP_400_BAD_REQUEST)

        actor = request.data['actor']

        movies_by_actor = self.queryset.filter(staff__staff__icontains=actor)
        serializer = MovieSerializer(data=movies_by_actor, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'], url_path='year')
    def get_movies_by_year_range(self, request):
        if 'minimumYear' not in request.data or 'maximumYear' not in request.data:
            return Response(status=HTTP_400_BAD_REQUEST)

        filtered_movies = self.queryset.all()
        if 'minimumYear' in request.data:
            minimum_year = request.data['minimumYear']
            filtered_movies = self.queryset.filter(year__gte=minimum_year)
        if 'maximumYear' in request.data:
            maximum_year = request.data['maximumYear']
            filtered_movies = filtered_movies.filter(year__lte=maximum_year)

        serializer = MovieSerializer(data=filtered_movies, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'], url_path='director')
    def get_movies_by_director(self, request):
        if 'director' not in request.data:
            return Response(status=HTTP_400_BAD_REQUEST)

        director = request.data['director']

        movies_by_director = self.queryset.filter(director__icontains=director)
        serializer = MovieSerializer(data=movies_by_director, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'], url_path='genre')
    def get_movies_by_genre(self, request):
        if 'genre' not in request.data:
            return Response(status=HTTP_400_BAD_REQUEST)
        genre = request.data['genre']

        movies_by_genre = self.queryset.filter(genre=genre)
        serializer = MovieSerializer(data=movies_by_genre, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)
