from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def watchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type = "application/xml")

def watchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

def watchlist_html(request):
    banyak_film_ditonton = 0
    data = MyWatchList.objects.all()
    for film in data:
        if film.watched == True:
            banyak_film_ditonton += 1
            
    context = {"watchlist": data, "banyak_film_ditonton": banyak_film_ditonton}
    return render(request, "mywatchlist.html", context)