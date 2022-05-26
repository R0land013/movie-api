from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from movie.models import Movie
from movie.serializers import MovieSerializer
from rest_framework.decorators import action


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'], url_path='by_country')
    def get_movies_by_country(self, request):
        country = request.data['country']

        movies_by_country = self.queryset.filter(country=country)
        serializer = MovieSerializer(data=movies_by_country, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'], url_path='by_actor')
    def get_movies_by_actor(self, request):
        actor = request.data['actor']

        movies_by_actor = self.queryset.filter(staff__staff__icontains=actor)
        serializer = MovieSerializer(data=movies_by_actor, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'], url_path='year')
    def get_movies_by_year_range(self, request):
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
