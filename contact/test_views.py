from django.test import TestCase


class TestViews(TestCase):
    """ Tests for contact views """

    def get_contact_form(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/contact/contact.html')
        