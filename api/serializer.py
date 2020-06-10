from rest_framework import serializers
from stadion.models import Stadion
from django.contrib.auth.models import User



class StadionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'