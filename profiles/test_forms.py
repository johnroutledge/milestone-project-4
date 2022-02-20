""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """ Tests for user profile form """
    def test_default_phone_number_is_not_required(self):
        """ Tests default_phone_number field is not required """
        form = UserProfileForm({'default_phone_number': ''})
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_default_street_address1_is_not_required(self):
        """ Tests default_street_address1 field is not required """
        form = UserProfileForm({'default_street_address1': ''})
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_default_street_address2_is_not_required(self):
        """ Tests default_street_address2 field is not required """
        form = UserProfileForm({'default_street_address2': ''})
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_default_town_or_city_is_not_required(self):
        """ Tests default_town_or_city field is not required """
        form = UserProfileForm({'default_town_or_city': ''})
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_default_county_is_not_required(self):
        """ Tests default_county field is not required """
        form = UserProfileForm({'default_county': ''})
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_default_postcode_is_not_required(self):
        """ Test default_postcode field is not required """
        form = UserProfileForm({'default_postcode': ''})
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_default_country_is_not_required(self):
        """ Test default_country field is not required """
        form = UserProfileForm({'default_country': ''})
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)
