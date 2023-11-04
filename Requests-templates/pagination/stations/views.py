import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', encoding='utf-8') as f:
        stations_file = csv.reader(f)
        stations_list = []
        for row in stations_file:
            stations_list.append({
                'Name': row[1],
                'Street': row[4],
                'District': row[6]
            })
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(stations_list[1:], 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page,
        }
    return render(request, 'stations/index.html', context)
