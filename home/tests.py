from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    """
    Test Home app
    """
    def test_home_page(self):
        """
        Test that the home page renders the correct template

        This test checks if the home page URL returns a 200 status code
        and uses the 'home/index.html' template.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
