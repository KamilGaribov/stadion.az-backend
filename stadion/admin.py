from django.contrib import admin
from .models import *

admin.site.register([Stadion, Hour, StadionFeedBack, StadionImage, Team])