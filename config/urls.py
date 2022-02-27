# from .blog.views import PostList

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostList.as_view() )
]
