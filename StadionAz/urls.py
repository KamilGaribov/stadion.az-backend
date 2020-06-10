from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace="main")),
    path('account/', include('account.urls', namespace='accunt')),
    path('stadion/', include('stadion.urls', namespace='stadion')),
    path('api/', include('api.urls', namespace='api')),
    path('team/', include('team.urls', namespace='team')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)