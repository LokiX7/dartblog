from django.db.models import Max, F
from django.views.generic import ListView, DetailView
from .models import Post, Tag, Category


class BaseIndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['pinned'] = context['posts'].first()
        return context

class BaseSingleView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


def get_pub_posts():
    """Return QuerySet with published posts"""
    return Post.objects.filter(is_published=True)

def get_category(category_slug):
    """Return category object by slug"""
    return Category.objects.get(slug=category_slug)

def get_pub_posts_by_category(category_obj):
    """Return QuerySet with published posts by category"""
    return Post.objects.filter(category=category_obj, is_published=True)

def get_tags():
    """Return QuerySet with all tags"""
    return Tag.objects.all()

def get_tag(tag_slug):
    """Return tag object by slug"""
    return Tag.objects.get(slug=tag_slug)

def get_pub_posts_by_tag(tag_obj):
    """Return QuerySet with published posts by tag"""
    return Post.objects.filter(tags=tag_obj, is_published=True)

def increase_post_views(object, value: int) -> None:
    """increases post views by a given value"""
    object.views = F('views') + value
    object.save()
    object.refresh_from_db()

#def get_most_rated_post(queryset):
#    """Return most rated post"""
#    max_rating = queryset.aggregate(max=Max('rating'))['max']
#    return queryset.get(rating=max_rating)
