from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from .views import QuestionViewSet
from apps.party.urls import router as party_router

urlpatterns = []

question_router = routers.NestedSimpleRouter(party_router, r'parties', lookup='party')
question_router.register('questions', QuestionViewSet, basename='question')


urlpatterns += question_router.urls
