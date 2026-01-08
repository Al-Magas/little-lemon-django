
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class MenuAPITest(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_user(
            username='admin',
            password='adminpass',
            is_staff=True
        )
        self.client.login(username='admin', password='adminpass')

    def test_create_menu(self):
        response = self.client.post('/api/menu/', {
            "name": "Pizza",
            "price": 12000,
            "menu_item_description": "Pizza du chef"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
