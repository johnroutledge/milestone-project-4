from django.db import models
from profiles.models import UserProfile

# Create your models here.


class Post(models.Model):
    """ The model for a news post """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """ to show most recent news posts first """
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ The model for a comment on a news post """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    comment_body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ to show most recent comments first """
        ordering = ['-date_created']

    def __str__(self):
        return 'Comment {} by {}'.format(
            self.comment_body, self.name, date_created)
