from django.shortcuts import render
from django.contrib.auth.models import User
from stadion.models import *


def TeamReg(request):
    if request.method == 'GET':
        return render(request,'teamreg.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        players = request.POST.getlist('player')
        if request.POST.get('bio'):
            bio = request.POST.get('bio')
            new = Team(name=name, city=city, bio=bio)
        else:
            new = Team(name=name, city=city)
        new.save()
        for i in players:
            player = User.objects.get(username=i)
            new.player.add(player)
        return render(request, 'home.html')

#