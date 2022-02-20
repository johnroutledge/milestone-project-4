""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from django.contrib.auth.models import User


class TestUserProfileModel(TestCase):
    """
    test the user profile model
    """
    def test_user_profile_string_method_returns_username(self):
        """
        Test the user profile string method returns the username
        """
        self.user = User.objects.create_user(
            username="test", password="Test123"
        )
        username = "test"
        self.assertEqual(username, str(self.user))
