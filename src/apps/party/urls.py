from rest_framework.routers import SimpleRouter

from .views import PartyViewSet

urlpatterns = []

router = SimpleRouter()
router.register('parties', PartyViewSet, basename='party')

urlpatterns += router.urls
