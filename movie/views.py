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
