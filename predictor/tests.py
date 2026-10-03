from django.test import TestCase, Client
from django.urls import reverse


class HomePageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_empty_form_submission(self):
        response = self.client.post(reverse('home'), {})
        self.assertEqual(response.status_code, 200)

    def test_invalid_completion_percentage(self):
        response = self.client.post(reverse('home'), {
            'completion_percentage': '150'
        })
        self.assertEqual(response.status_code, 200)
