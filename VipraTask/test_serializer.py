import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contactbook.settings')
django.setup()
from feed.serializers import ContactBookSerializer
import unittest
from django.test import TestCase

class TestView(TestCase):
    def test_add_contact(self):    
        response = ContactBookSerializer(data={
            'first_name': 'Boranescu1',
            'last_name': 'Alexandru1', 
            'email': 'boranescu.alex1@yahoo.com', 
            'phoneNumber': '0747843760'
        })
        self.assertTrue(response.is_valid())

if __name__ == '__main__':
    unittest.main()