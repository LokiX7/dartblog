from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Post, Tag, Category

class Index(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class ByCategory(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = False
    
    def get_queryset(self, **kwargs):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        self.category_obj = Category.objects.get(slug=self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context['title'] = self.category_obj.title
        return context


def foo(request):
    return render(request, 'blog/index.html')

