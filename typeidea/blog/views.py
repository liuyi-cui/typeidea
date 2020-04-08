from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post, Tag, Category
from config.models import SiderBar

# Create your views here.
def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.lastest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SiderBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)




class PostDetailView(DetailView):
    # queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    model = Post
    template_name = 'blog/detail.html'
