from django.contrib import admin
from django.urls import path, include

api = [
    path('', include('apps.authentication.urls')),
    path('', include('apps.present.urls')),
    path('', include('apps.party.urls')),
    path('', include('apps.question.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
]
