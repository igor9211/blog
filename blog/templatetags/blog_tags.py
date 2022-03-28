from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import datetime
import markdown

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# nie uzywane bo dluzsze i bez sensu
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.inclusion_tag('blog/post/most_commented_posts2.html')
def get_most_commented_posts2(count=5):
    best_commented = Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return {'best_commented': best_commented}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.filter(name='date')
def date_format(date):
    date = datetime.datetime.strftime(date, "%Y-%m-%d")
    return date


@register.filter
def total_amount(arg):
    return len(arg)


@register.inclusion_tag('blog/post/search.html')
def show_search():
    view.post
    return {'latest_posts': latest_posts}