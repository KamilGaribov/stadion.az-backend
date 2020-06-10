from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Min, Max, Sum, Avg
from .models import *
from django.contrib.auth.models import User



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

def StadionList(request):
    model = Stadion.objects.all()
    paginator = Paginator(model, 1)
    page_request = 'page'
    page = request.GET.get(page_request)
    try:
        eachpage = paginator.page(page)
    except PageNotAnInteger:
        eachpage = paginator.page(1)
    except EmptyPage:
        eachpage = paginator.page(paginator.num_pages)
    
    arr = []
    for i in range(0, eachpage.paginator.num_pages):
        arr.append(i+1)
    
    context = {
        'stadion': eachpage,
        'page': page_request,
        'paginator': arr,
        'city': city,
        'district': district,
        'metro': metro,
        'floor': floor,
        'size': size,
    }
    return render(request, 'stadion.html', context)

def StadionDirect(request, pk):
    stadion = Stadion.objects.get(pk=pk)
    hour = Hour.objects.filter(stadion=stadion)
    image = StadionImage.objects.filter(stadion=stadion)
    feedback = StadionFeedBack.objects.filter(stadion=stadion)

    context = {
        'stadion': stadion,
        'hour': hour,
        'image': image,
        'feedback': feedback
    }
    return render(request, 'direct.html', context)

def StadionFilter(request):    
    day = ''
    hour = ''
    if request.GET.get('day') or request.GET.get('hour'):
        day = request.GET.get('day')
        hour = request.GET.get('hour')
        boool = 'False'
        data = Hour.objects.all()
        if day:
            data = data.filter(day=day)
        if hour:
            data = data.filter(**{hour: boool})
        
        ids = data.values_list('stadion', flat=True)
        sent_data = Stadion.objects.filter(id__in=ids)

        context = {
            'city': city,
            'district': district,
            'metro': metro,
            'floor': floor,
            'size': size,
            'day': day,
            'hour': hour,
            'data': sent_data
        }
        return render(request, 'filter.html', context)


    
    if request.GET.get('search'):
        search_query = request.GET.get('search')
        sent_data = Stadion.objects.filter(name__icontains=search_query)
        context = {
            'city': city,
            'district': district,
            'metro': metro,
            'floor': floor,
            'size': size,
            'data': sent_data
        }
        return render(request, 'filter.html', context)


    sent_data = Stadion.objects.all()

    city_arr = Stadion.objects.values_list('city', flat=True)
    district_arr = Stadion.objects.values_list('district', flat=True)
    metro_arr = Stadion.objects.values_list('metro', flat=True)
    floor_arr = Stadion.objects.values_list('floor', flat=True)
    size_arr = Stadion.objects.values_list('size', flat=True)

    city_query = request.GET.get('city')
    district_query = request.GET.get('district')
    metro_query = request.GET.get('metro')
    floor_query = request.GET.get('floor')
    size_query = request.GET.get('size')
    cover_query = request.GET.get('cover')
    cafe_query = request.GET.get('cafe')
    park_query = request.GET.get('park')
    video_query = request.GET.get('video')
    min_query = request.GET.get('min')
    max_query = request.GET.get('max')

    if city_query and city_query not in city_arr:
        return render(request, 'notfound.html')
    elif district_query and district_query not in district_arr:
        return render(request, 'notfound.html')
    elif metro_query and metro_query not in metro_arr:
        return render(request, 'notfound.html')
    elif floor_query and floor_query not in floor_arr:
        return render(request, 'notfound.html')
    elif size_query and size_query not in size_arr:
        return render(request, 'notfound.html')

    if min_query and min_query.isnumeric() == False:
        return render(request, 'notfound.html')
    if max_query and max_query.isnumeric() == False:
        return render(request, 'notfound.html')
    
    if cover_query == 'on':
        sent_data = sent_data.filter(cover=True)
    elif cover_query and cover_query != 'on':
        return render(request, 'notfound.html')
    if cafe_query == 'on':
        sent_data = sent_data.filter(cafe=True)
    elif cafe_query and cafe != 'on':
        return render(request, 'notfound.html')
    if park_query == 'on':
        sent_data = sent_data.filter(park=True)
    elif park_query and park_query != 'on':
        return render(request, 'notfound.html')
    if video_query == 'on':
        sent_data = sent_data.filter(video=True)
    elif video_query and video_query != 'on':
        return render(request, 'notfound.html')

    if min_query == '':
        min_query = Stadion.objects.aggregate(Min('price'))['price__min']
    if max_query == '':
        max_query = Stadion.objects.aggregate(Max('price'))['price__max']
    min_query = int(min_query)-1
    max_query = int(max_query)+1

    if city_query:
        sent_data = sent_data.filter(city=city_query)
    if district_query:
        sent_data = sent_data.filter(district=district_query)
    if metro_query:
        sent_data = sent_data.filter(metro=metro_query)
    if floor_query:
        sent_data = sent_data.filter(floor=floor_query)
    if size_query:
        sent_data = sent_data.filter(size=size_query)
    sent_data = sent_data.filter(price__range=(min_query, max_query))


    
    context = {
        'data': sent_data,
        'city': city,
        'district': district,
        'metro': metro,
        'floor': floor,
        'size': size,
    }
    return render(request, 'filter.html', context)

def StadionOrder(request, pk):
    day = request.GET.get('day')
    hour = request.GET.get('hour')
    z = Hour.objects.get(stadion=pk, day=day)
    stadion = Stadion.objects.get(id=pk)
    count = stadion.ordered
    count += 1
    stadion.ordered = count
    stadion.save()

    if hour == '21':
        z.nine = True
        z.save()
    elif hour == '22':
        z.ten = True
        z.save()
    elif hour == '23':
        z.eleven = True
        z.save()
    elif hour == '24':
        z.twelve = True
        z.save()
    
    context = { 
        'day': day,
        'hour': hour,
        'id': pk
    }
    return render(request, 'order.html', context)

def FeedBack(request, pk):
    user = User.objects.get(id=request.user.id)
    stadion = Stadion.objects.get(id=pk)
    star = request.GET.get('star')
    if request.GET.get('comment'):
        comment = request.GET.get('comment')
    new = StadionFeedBack(user=user, stadion=stadion, stars=star, comment=comment)
    new.save()

    feedback = StadionFeedBack.objects.filter(stadion=stadion)
    count = feedback.count()
    summary = feedback.aggregate(Sum('stars'))
    x = round(summary['stars__sum']/count)
    stadion.star = x
    stadion.save()
    return render(request, 'home.html')

#