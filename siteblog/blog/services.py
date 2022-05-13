from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category


class BaseIndex(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2
    

def get_posts_by_category(category_slug):
    return Post.objects.filter(category__slug=category_slug)

def get_category(category_slug):
    return Category.objects.get(slug=category_slug)
