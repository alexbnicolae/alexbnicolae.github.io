import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contactbook.settings')
django.setup()
from feed.serializers import ContactBookSerializer
import unittest
from django.test import TestCase

class TestView(TestCase):
    

    def test_home_page(self):
        response = self.client.get('/contacts', follow=True)
        # print("print:", response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_info_contact(self):
        response = self.client.get('/contacts/12', follow=True)
        self.assertEqual(response.status_code, 200)
    
    


    def test_delete_contact(self):
        response = self.client.delete('/contacts/12')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

