from django.contrib import admin
from Blog_System.blogs.models import Blog, Post, Comment


class PostInLine(admin.StackedInline):
    model = Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    inlines = (PostInLine, )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post)
admin.site.register(Comment)

