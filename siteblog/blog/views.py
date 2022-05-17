from django.shortcuts import render

from blog import services, baseViews

class Home(baseViews.BaseIndexView):
    title = 'Home'


class ByCategory(baseViews.BaseIndexView):   
    allow_empty = True
    
    def get_queryset(self):
        category = services.get_category(self.kwargs['slug'])
        self.title = category.title
        return services.get_pub_posts_by_category(category)


class ByTag(baseViews.BaseIndexView):   
    allow_empty = True
    
    def get_queryset(self):
        tag = services.get_tag(self.kwargs['slug'])
        self.title = tag.title
        return services.get_pub_posts_by_tag(tag)


class GetPost(baseViews.BaseSingleView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = services.get_tags()
        services.increase_post_views(self.object, 1)
        return context

