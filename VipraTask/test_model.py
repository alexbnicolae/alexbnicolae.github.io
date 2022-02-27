from dataclasses import field
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contactbook.settings')
django.setup()
from django.test import TestCase

from feed.models import ContactBook
import unittest
class ContactBookTest(TestCase):

    def test_first_name_label(self):
        contactBook = ContactBook.objects.get(id=12)
        field_label = contactBook._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_phone_number_label(self):
        contactBook = ContactBook.objects.get(id=12)
        self.assertEqual(contactBook.phoneNumber, '0747843732')

if __name__ == '__main__':
    unittest.main()