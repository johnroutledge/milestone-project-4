# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase
from django.shortcuts import reverse


class TestViews(TestCase):
    """ Tests for basket views """
    def test_basket_url_exists(self):
        """
        Test that the basket page URL exists
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)

    def test_basket_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get(reverse('view_basket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='basket/basket.html')

    def test_basket_page_is_accessible_by_name(self):
        """
        test the basket page is accessible by name
        """
        response = self.client.get(reverse('view_basket'))
        self.assertEqual(response.status_code, 200)
