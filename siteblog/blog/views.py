from django.shortcuts import render

from blog import services

class Index(services.BaseIndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class ByCategory(services.BaseIndexView):
    template_name = 'blog/category.html'
    allow_empty = True
    
    def get_queryset(self, **kwargs):
        super().get_queryset(**kwargs)
        return services.get_posts_by_category(self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = services.get_category(self.kwargs['slug']).title
        return context


def foo(request):
    return render(request, 'blog/index.html')

