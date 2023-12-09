from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post, Comment, Category
from django.contrib.auth.models import User


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def index(request):
    return render(request, 'index.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})


def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def blog_details(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blogdetails.html', {'post': post})
