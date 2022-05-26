from rest_framework import routers
from movie.views import MovieViewSet


router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)

urlpatterns = router.urls
