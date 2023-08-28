from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from apps.authentication.views import UserViewSet

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns += router.urls
