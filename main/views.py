from django.shortcuts import render
from stadion.models import *


def home(request):
    data = Stadion.objects.all()
    city = []
    district = []
    metro = []
    floor = []
    size = []

    for i in data:
        if i.city not in city:
            city.append(i.city)
        if i.district not in district:
            district.append(i.district)
        if i.metro not in metro and i.metro != None:
            metro.append(i.metro)
        if i.floor not in floor:
            floor.append(i.floor)
        if i.size not in size:
            size.append(i.size)
    

    days =  Hour.objects.values_list('day', flat=True)
    day = []
    for i in days:
        if i not in day:
            day.append(i)
    hour = ['nine', 'ten', 'eleven', 'twelve']
    context = {
        'city': city,
        'district': district,
        'metro': metro,
        'floor': floor,
        'size': size,
        'day': day,
        'hour': hour
    }
    return render(request, 'home.html', context)