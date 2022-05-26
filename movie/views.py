from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from movie.models import Movie
from movie.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]