from rest_framework.routers import SimpleRouter

from .views import PresentViewSet

urlpatterns = []

router = SimpleRouter()
router.register('presents', PresentViewSet, basename='present')

urlpatterns += router.urls
