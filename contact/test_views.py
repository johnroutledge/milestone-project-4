# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase
from django.shortcuts import reverse

from .views import contact


class TestViews(TestCase):
    """ Tests for contact views """
    def test_get_contact_form(self):
        """
        Test that contact view responds correctly
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="contact/contact.html")


    def test_contact_page_url_exists(self):
        """
        Test that the contact page URL exists
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)


    def test_contact_page_is_accessible_by_name(self):
        """
        test the contact page is accessible by name
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)