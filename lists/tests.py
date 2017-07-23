from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class SmokeTest(TestCase):

    def test_root_url_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)
