"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase


class ViewTest(TestCase):
    def test_home(self):
        self.client.get('/')

    def test_info(self):
        self.client.get('/info/')

    def test_chart(self):
        self.client.get('/chart.js')
