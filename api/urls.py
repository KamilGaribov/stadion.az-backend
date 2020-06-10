from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('', StadionApi)
user = routers.DefaultRouter()
user.register('', UserApi)

urlpatterns = [
    path('stadion/', include(router.urls)),
    path('user/', include(user.urls)),
]