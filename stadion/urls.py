from django.urls import path, include, re_path
from .views import *

app_name = 'stadion'

urlpatterns = [
    path('', StadionList, name='home'),
    path('detail/id=<int:pk>', StadionDirect, name='detail'),
    path('filter/', StadionFilter, name='filter'),
    path('order/id=<int:pk>', StadionOrder, name='order'),
    path('feedback/id=<int:pk>', FeedBack, name='feedback')
]