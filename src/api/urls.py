from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

api = [
    path('', include('apps.authentication.urls')),
    path('', include('apps.present.urls')),
    path('', include('apps.party.urls')),
    path('', include('apps.question.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
