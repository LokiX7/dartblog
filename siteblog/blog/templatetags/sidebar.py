from django import template

from blog import services


register = template.Library()

@register.inclusion_tag('blog/tags_tpl/_posts_tags.html')
def show_tags(cnt=10):
    tags = services.get_tags_ordered_by_num_of_posts()[:cnt]
    return {'tags': tags}

@register.inclusion_tag('blog/tags_tpl/_most_viewed.html')
def show_popular(cnt=3):
    posts = services.get_posts_ordering('-views')[:cnt]
    return {'posts': posts}
