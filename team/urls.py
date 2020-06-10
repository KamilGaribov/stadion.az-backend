from django.urls import path
from .views import *

app_name = 'team'

urlpatterns = [
    path('registration/', TeamReg, name='reg'),
]