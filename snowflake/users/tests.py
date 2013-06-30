"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import unittest
from django.core.management import call_command
#from django.test import TestCase


class SimpleTest(unittest.TestCase):

    def setup(self):
        call_command("test")
        
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        print "AAA"
        self.assertEqual(1 + 1, 2)
