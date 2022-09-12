from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def katalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_item' : data_katalog_item,
        'nama' : 'Farkhan Syawal Harahap',
        'id' : 2106709125
    }
    return render(request, "katalog.html", context)