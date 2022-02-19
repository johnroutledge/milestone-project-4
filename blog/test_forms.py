# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase
from .forms import CommentForm, PostForm


class TestCommentForm(TestCase):
    """ Tests for comment form """
    def test_name_is_required(self):
        """ Tests name field is required """
        form = CommentForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
                         form.errors['name'][0],
                         'This field is required.'
        )

    def test_comment_body_is_required(self):
        """ Tests comment_body field is required """
        form = CommentForm({'comment_body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment_body', form.errors.keys())
        self.assertEqual(
                         form.errors['comment_body'][0],
                         'This field is required.'
        )

class TestPostForm(TestCase):
    """ Tests for post form """
    def test_title_is_required(self):
        """ Test title field is required """
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(
                         form.errors['title'][0],
                         'This field is required.'
        )

    def test_slug_is_required(self):
        """ Test slug field is required """
        form = PostForm({'slug': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(
                         form.errors['slug'][0],
                         'This field is required.'
        )

    def test_author_is_required(self):
        """ Test author field is required """
        form = PostForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(
                         form.errors['author'][0],
                         'This field is required.'
        )

    def test_content_is_required(self):
        """ Test content field is required """
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(
                         form.errors['content'][0],
                         'This field is required.'
        )
