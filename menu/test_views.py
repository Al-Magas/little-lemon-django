# menu/tests.py
from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
