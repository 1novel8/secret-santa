from rest_framework.routers import SimpleRouter
from .views import QuestionViewSet

urlpatterns = []

router = SimpleRouter()
router.register('questions', QuestionViewSet, basename='question')

urlpatterns += router.urls
