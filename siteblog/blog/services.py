from django.db.models import Max, Count, F
from .models import Post, Tag, Category

def get_pub_posts():
    """Return QuerySet with published posts"""
    return Post.objects.filter(is_published=True)

def get_category(category_slug):
    """Return category object by slug"""
    return Category.objects.get(slug=category_slug)

def get_categories():
    """Return QuerySet with all categories"""
    return Category.objects.all()

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

def get_posts_ordering(*args):
    """Return posts that are sorted by args values"""
    return Post.objects.order_by(*args)

def get_tags_ordered_by_num_of_posts():
    """Return tags ordered by num of posts"""
    return get_tags().annotate(num=Count('posts')).order_by('-num')
