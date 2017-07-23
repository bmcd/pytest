from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class SmokeTest(TestCase):

    def test_root_url_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
