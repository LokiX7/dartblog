from django.shortcuts import render
from django.views.generic import ListView
from blog import services, baseviews

class Home(baseviews.BaseIndexView):
    title = 'Home'


class ByCategory(baseviews.BaseIndexView):   
    allow_empty = True
    
    def get_queryset(self):
        category = services.get_category(self.kwargs['slug'])
        self.title = category.title
        return services.get_pub_posts_by_category(category)


class ByTag(baseviews.BaseIndexView):   
    allow_empty = True
    
    def get_queryset(self):
        tag = services.get_tag(self.kwargs['slug'])
        self.title = tag.title
        return services.get_pub_posts_by_tag(tag)


class GetPost(baseviews.BaseSingleView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services.increase_post_views(self.object, 1)
        return context


class Search(ListView):
    template_name = 'blog/search_result.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.key = self.request.GET.get('s')
        result = services.search_posts(self.key)
        self.count = result['count']
        return result['queryset']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search'
        context['key'] = self.key
        context['count'] = self.count
        return context

