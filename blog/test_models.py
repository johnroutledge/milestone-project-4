# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase
from .models import Post


class TestPostModel(TestCase):
    """ tests post model """
    def test_post_string_method(self):
        """
        test order post string method
        """
        post = Post.objects.create(title="test_post")
        self.assertEqual(str(post), "test_post")
