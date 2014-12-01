from django.test import TestCase
from django.core.urlresolvers import resolve

from .views import createworkpack


class WorkpackTests(TestCase):
    def test_work_pack_create_page_is_loading_correct_url(self):
        found = resolve('createworkpack')
        self.assertEqual(found.func, createworkpack)