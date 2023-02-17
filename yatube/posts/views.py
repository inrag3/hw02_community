from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    # TODO Переопределить Meta класс модели, чтобы сортировка была по умолчанию

    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    # Наверно стоит вынести повторяющиеся код
    post_list = group.posts.order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    context = {

    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    count = Post.objects.all().filter(author=post.author).count()
    context = {
        'post': post,
        'count': count,
    }
    return render(request, 'posts/post_detail.html', context)
