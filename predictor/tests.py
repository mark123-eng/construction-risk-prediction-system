from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):

    def setUp(self):
        self.url = reverse("home")
        self.https_headers = {
            "HTTP_X_FORWARDED_PROTO": "https",
        }

    def test_home_page_loads(self):
        response = self.client.get(
            self.url,
            secure=True,
            **self.https_headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_empty_form_submission(self):
        response = self.client.post(
            self.url,
            {},
            secure=True,
            **self.https_headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_invalid_completion_percentage(self):
        response = self.client.post(
            self.url,
            {
                "completion_percentage": "150",
            },
            secure=True,
            **self.https_headers,
        )

        self.assertEqual(response.status_code, 200)
