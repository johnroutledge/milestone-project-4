from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post

from profiles.models import UserProfile

from .forms import CommentForm, PostForm

   

# Create your views here.


def blog(request):
    """ Display all blog posts """

    posts = Post.objects.all()
    post_count = len(posts)
    template = 'blog/blog.html'
    context = {
        'posts': posts,
        'post_count': post_count
    }
    return render(request, template, context)


def blog_post_detail(request, slug):
    """ Display full blog post plus any comments """
    post = Post.objects.get(slug=slug)
    comments = post.comments

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('blog_post_detail', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/blog_post_detail.html'
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'on_blog_page': True,
    }

    return render(request, template, context)


@login_required
def add_blog_post(request):
    """ Add blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Jiira admin access only.')
        return redirect(reverse('homepage'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post successfully added.')
            return redirect(reverse('blog_post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Unable to add blog post. Please check form validity.')
    else:
        form = PostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
        'on_blog_page': True,
    }

    return render(request, template, context)


@login_required
def edit_blog_post(request, slug):
    """ Edit blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Jiira admin access only.')
        return redirect(reverse('homepage'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post successfully edited.')
            return redirect(reverse('blog_post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Unable to update blog post. Please check form validity.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'Now editing {post.title}')

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'post': post,
        'on_blog_page': True,
    }

    return render(request, template, context)


@login_required
def delete_blog_post(request, slug):
    """ Delete blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Jiira admin access only.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post successfully deleted.')
    return redirect(reverse('blog'))