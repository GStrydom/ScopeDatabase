from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from .views import homepageview


class HomePageTests(TestCase):
    def test_home_page_url_is_correct(self):
        page_found = resolve('/')
        self.assertEqual(page_found.func, homepageview)

    def test_available_workpacks_are_being_initially_loaded(self):
        pass