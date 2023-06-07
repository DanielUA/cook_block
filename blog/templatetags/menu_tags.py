from django import template
from blog.models import Category, Post

register = template.Library()

def get_all_catigories():
    return Category.objects.all()

@register.simple_tag()
def get_list_category():
    """return all categories"""
    return get_all_catigories()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.all()
    return {"list_category": category}


@register.inclusion_tag('blog/include/tags/pecipes_tag.html')
def get_last_posts():
    posts = Post.objects.select_related("category").order_by("-id")[:5]
    return {"list_last_post": posts}
