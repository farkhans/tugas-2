from django.test import TestCase
from katalog.models import CatalogItem
# Create your tests here.
class CatalogTestCase(TestCase):

    def test_create_catalog(self):
        test = CatalogItem.objects.create(
            item_name = "iPhone 12 Pro Max",
            item_price = 17999999,
            item_stock = 3,
            description = "Original from iBox",
            rating = 5,
            item_url = "https://www.tokopedia.com/ptpratamasemesta/iphone-12-pro-max-garansi-resmi-ibox-silver-256-gb"
            )
        self.assert_(test.item_name == "iPhone 12 Pro Max")
        self.assert_(test.item_price == 17999999)
        self.assert_(test.item_stock == 3)
        self.assert_(test.description == "Original from iBox")
        self.assert_(test.rating == 5)
        self.assert_(test.item_url == "https://www.tokopedia.com/ptpratamasemesta/iphone-12-pro-max-garansi-resmi-ibox-silver-256-gb")