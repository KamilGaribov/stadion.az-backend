from django.shortcuts import render
from rest_framework import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from stadion.models import Stadion
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated


class StadionApi(ReadOnlyModelViewSet):
    queryset = Stadion.objects.all()
    serializer_class = StadionSerializer

    def get_queryset(self):
        name = self.request.GET.get('search')
        if name:
            return Stadion.objects.filter(name__icontains=name)
        return super().get_queryset()

class UserApi(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        name = self.request.GET.get('search')
        if name:
            return User.objects.filter(username__icontains=name)
        return super().get_queryset()