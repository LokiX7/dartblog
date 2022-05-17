from django import template

from blog import services


register = template.Library()

@register.inclusion_tag('blog/tags_tpl/_menu.html')
def show_menu(menu_class='menu'):
    categories = services.get_categories()
    return {'menu_categories': categories, 'menu_class': menu_class}
