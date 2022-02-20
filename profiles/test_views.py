""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase, Client

from django.shortcuts import reverse
from django.contrib.auth.models import User


class TestProfileViews(TestCase):
    """
    Test the profile page loads correctly
    """
    def test_profile_page_url_exists(self):
        """
        Test the url works when loading the page
        """
        self.user = User.objects.create_user(
            username="test", password="Test123", email="test@test.com"
        )
        self.client.login(username="test",
                          email="test@test.com", password="Test123")
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_view_uses_correct_template(self):
        """
        test correct template is used
        """
        self.user = User.objects.create_user(
            username="test", password="Test123", email="test@test.com"
        )
        self.client.login(username="test",
                          email="test@test.com", password="Test123")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='profiles/profile.html')

    def test_profile_page_is_accessible_by_name(self):
        """
        test profile page is accessible by name
        """
        self.user = User.objects.create_user(
            username="test", password="Test123", email="test@test.com"
        )
        self.client.login(username="test",
                          email="test@test.com", password="Test123")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
