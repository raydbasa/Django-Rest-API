from django.contrib import admin
from .models import Post, Comment, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_published')


admin.site.register(Post)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'date_posted')


admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Category)
