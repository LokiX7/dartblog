from django import template

from blog.models import Category


register = template.Library()

@register.inclusion_tag('blog/_menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'menu_categories': categories, 'menu_class': menu_class}
