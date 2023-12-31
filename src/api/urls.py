from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView
from django.conf import settings


api = [
    path('', include('apps.authentication.urls')),
    path('', include('apps.present.urls')),
    path('', include('apps.party.urls')),
    path('', include('apps.question.urls')),
]

urlpatterns = [
    # documentation
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # general
    path('admin/', admin.site.urls),
    path('api/', include(api)),
    # django-debug-toolbar
    path('__debug__/', include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
