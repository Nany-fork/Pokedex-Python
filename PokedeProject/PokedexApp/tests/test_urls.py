from django.test import SimpleTestCase
from django.urls import reverse, resolve
from PokedexApp.views import index

class TestsPokedexAppUrls(SimpleTestCase):
    def test_list_urls_is_resolve(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)