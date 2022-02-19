# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase
from django.shortcuts import reverse

from .models import Post

class TestViews(TestCase):
    """ Tests for blog views """
    def test_blog_page_url_exists(self):
        """
        Test that blog page URL exists
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_view_uses_correct_template(self):
        """
        Test that correct template is used
        """
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='blog/blog.html')

    def test_blog_page_is_accessible_by_name(self):
        """
        test blog page is accessible by name
        """
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_blog_posts(self):
        """
        Test that blog post can be retrieved
        """
        posts = Post.objects.all()
        for post in posts:
            response = self.client.get(reverse('posts'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, post.id)

    def test_blog_post_detail_page_url_exists(self):
        """
        test blog post detail page loads via url
        """
        post = Post.objects.create(slug='testpost')
        response = self.client.get(f'/blog/{post.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_blog_post_detail_page_template(self):
        """
        test blog post detail page loads via template
        """
        post = Post.objects.create(slug='testpost')
        response = self.client.get(f'/blog/{post.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_post_detail.html')
