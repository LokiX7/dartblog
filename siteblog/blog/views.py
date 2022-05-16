from django.shortcuts import render

from blog import services

class Home(services.BaseIndexView):
    title = 'Home'


class ByCategory(services.BaseIndexView):   
    allow_empty = True
    
    def get_queryset(self):
        category = services.get_category(self.kwargs['slug'])
        self.title = category.title
        return services.get_pub_posts_by_category(category)


class ByTag(services.BaseIndexView):   
    allow_empty = True
    
    def get_queryset(self):
        tag = services.get_tag(self.kwargs['slug'])
        self.title = tag.title
        return services.get_pub_posts_by_tag(tag)


class GetPost(services.BaseSingleView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = services.get_tags()
        services.increase_post_views(self.object, 1)
        return context


def foo(request):
    return render(request, 'blog/index.html')

