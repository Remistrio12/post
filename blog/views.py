from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View

from blog.models import Post


class PostList(View):
    def get (self, request):
        posts = Post.objects.order_by('author')
        # paginator = Paginator(posts,4)
        # page = request.GET.get('page',1)
        # #page_obj = paginator.get_page(page)
        #
        # try:
        #     page_obj = paginator.get_page(page)
        # except PageNotAnInteger:
        #     page_obj = paginator.get_page(1)
        # except EmptyPage:
        #     page_obj = paginator.get_page(paginator.num_pages)
        ctx = {
               'posts': posts}
        return render(request, 'blog.html', ctx)
