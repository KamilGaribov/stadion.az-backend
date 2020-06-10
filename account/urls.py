from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_page, name='logout'),
]