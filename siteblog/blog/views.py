from django.shortcuts import render

from blog.services import BaseIndex, get_posts_by_category, get_category

class Index(BaseIndex):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class ByCategory(BaseIndex):
    template_name = 'blog/category.html'
    allow_empty = False
    
    def get_queryset(self, **kwargs):
        return get_posts_by_category(self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_category(self.kwargs['slug']).title
        return context


def foo(request):
    return render(request, 'blog/index.html')

