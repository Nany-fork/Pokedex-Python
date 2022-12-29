from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from PokedexApp.views import index

class TestViews(TestCase):
    def test_index_function(self):
        data={
            'pokemon':'ditto'
        }
        response = self.client.post(reverse(index), data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['name'], 'Ditto')
        
    def test_index_function_not_found_pokemon(self):
        data={
            'pokemon':'jsjsjsj'
        }
        response = self.client.post(reverse(index), data)
        self.assertEquals(response.status_code, 404)
        # self.assertEquals(response.context['name'], 'Ditto')