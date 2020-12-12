from django import template
from django.urls import reverse_lazy
from Blog_System.common.utils import can_user_create_blogs

register = template.Library()


@register.inclusion_tag('partials/create_blog.html')
def create_blog(user):
    return {
        'disabled': not can_user_create_blogs(user)
    }
