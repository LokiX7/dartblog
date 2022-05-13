from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Post, Tag, Category


class BaseIndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2
    

def get_posts(status):
    """return query with a given status"""
    return Post.objects.filter(status=status)

def get_posts_by_category(category_slug):
    """return published and pinned posts by category"""
    return Post.objects.filter(Q(category__slug=category_slug), ~Q(status=Post.UNPUBLISHED))

def get_category(category_slug):
    """return category object by slug"""
    return Category.objects.get(slug=category_slug)
