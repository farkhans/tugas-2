from django.urls import path
from mywatchlist.views import watchlist_html, watchlist_json, watchlist_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('', watchlist_html, name = "watchlist_html"),
    path('html/', watchlist_html, name = "watchlist_html"),
    path("xml/", watchlist_xml, name = "watchlist_xml"),
    path("json/", watchlist_json, name = "watchlist_json"),
]