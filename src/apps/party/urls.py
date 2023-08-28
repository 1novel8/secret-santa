from rest_framework.routers import SimpleRouter

from apps.party.views import PartyViewSet

urlpatterns = []

router = SimpleRouter()
router.register('parties', PartyViewSet, basename='party')

urlpatterns += router.urls
