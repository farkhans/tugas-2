from django.test import TestCase, Client
from django.urls import resolve
from mywatchlist.views import *

# Create your tests here.
class MyWatchListTest(TestCase):
    def test_watchlist_xml(self):
        response = Client().get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)

    def test_watchlist_html(self):
        response = Client().get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)
        
    def test_watchlist_json(self):
        response = Client().get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)