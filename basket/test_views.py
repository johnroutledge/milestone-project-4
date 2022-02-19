# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from .views import view_basket, add_to_basket

class TestViews(TestCase):
    """ Tests for basket views """
    def test_basket_url_exists(self):
        """
        Test that basket page URL exists
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)

    def test_basket_view_uses_correct_template(self):
        """
        Test that correct template is used
        """
        response = self.client.get(reverse('view_basket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='basket/basket.html')

    def test_basket_page_is_accessible_by_name(self):
        """
        test that basket page is accessible by name
        """
        response = self.client.get(reverse('view_basket'))
        self.assertEqual(response.status_code, 200)

    def test_view_basket(self):
        """
        test that view_basket view works correctly
        """
        link = reverse('view_basket')
        self.assertEqual(resolve(link).func, view_basket)
        response = self.client.get(reverse('view_basket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="basket/basket.html")

    def test_add_to_basket(self):
        """
        Test that add to bag view works correctly
        """
        link = reverse('add_to_basket', args=['item_id'])
        self.assertEqual(resolve(link).func, add_to_basket)
        response = self.client.get(reverse('view_basket'))
        self.assertEqual(response.status_code, 200)
