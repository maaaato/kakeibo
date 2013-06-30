"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from receipt.models import Receipt


class SimpleTest(TestCase):

    fixtures = ['init.json']

    #def setUp(self):
        #management.call_command('loaddata', 'init.json')

