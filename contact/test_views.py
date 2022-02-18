from django.test import TestCase

from django.urls import reverse, resolve

from .views import contact


class TestViews(TestCase):
    """ Tests for contact views """
    def get_contact_form(self):
        """
        Test that contact view responds correctly
        """
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="contact/contact.html")
