from django.urls import path
from .views import index, user_list, blog_list, comment_list, category_list, blog_details

urlpatterns = [
    path('', index, name='index'),
    path('users/', user_list, name='users'),
    path('blogs/', blog_list, name='blogs'),
    path('comments/', comment_list, name='comments'),
    path('categories/', category_list, name='categories'),
    path('blog/<int:post_id>/', blog_details, name='blog_details'),
]
