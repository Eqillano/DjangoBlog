from django import template

from blog.models import Category

register = template.library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {"categories":categories,"menu_class":menu_class}
