from rest_framework.routers import SimpleRouter
from apps.question.views import QuestionViewSet

urlpatterns = []

router = SimpleRouter()
router.register('questions', QuestionViewSet, basename='question')

urlpatterns += router.urls
