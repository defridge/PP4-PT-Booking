from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """
    Test Home app
    """
    def test_home_page(self):
        """ Test home page renders correct page """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
