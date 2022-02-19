# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """ Tests for order form """
    def test_full_name_is_required(self):
        """ Test full name field is required """
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
                         form.errors['full_name'][0],
                         'This field is required.'
        )

    def test_email_is_required(self):
        """ Test email field is required """
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
                         form.errors['email'][0],
                         'This field is required.'
        )

    def test_phone_number_is_required(self):
        """ Test phone number field is required """
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
                         form.errors['phone_number'][0],
                         'This field is required.'
        )

    def test_street_address1_is_required(self):
        """ Test street address 1 field is required """
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
                         form.errors['street_address1'][0],
                         'This field is required.'
        )

    def test_street_address2_is_not_required(self):
        """ Test street address 2 field is not required """
        form = OrderForm({'street_address2': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('street_address2', form.errors.keys())
        
    def test_town_or_city_is_required(self):
        """ Test town or city field is required """
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
                         form.errors['town_or_city'][0],
                         'This field is required.'
        )

    def test_county_is_not_required(self):
        """ Test county field is not required """
        form = OrderForm({'county': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('county', form.errors.keys())

    def test_postal_code_is_not_required(self):
        """ Test postal_code field is not required """
        form = OrderForm({'postal_code': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('postal_code', form.errors.keys())

    def test_country_is_required(self):
        """ Test country field is required """
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
                         form.errors['country'][0],
                         'This field is required.'
        )