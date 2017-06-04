"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase


class ViewTest(TestCase):
    fixtures = ['test.json']

    def test_home(self):
        response = self.client.get('/')
        self.assertContains(response, 'Bohuslav Sobotka')

    def test_info(self):
        self.client.get('/info/')

    def test_chart(self):
        response = self.client.get('/chart.js')
        self.assertContains(response, 'Rok')

    def test_ministri(self):
        response = self.client.get('/ministri/')
        self.assertContains(response, 'Bohuslav Sobotka')

    def test_ministr(self):
        response = self.client.get('/ministri/bohuslav-sobotka/')
        self.assertContains(response, 'Bohuslav Sobotka')
