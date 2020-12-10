from django.shortcuts import render
from django.views import generic as views
from Blog_System.blogs.models import Blog


class BlogsListView(views.ListView):
    template_name = 'blogs/list.html'
    model = Blog


class BlogDetailView(views.DetailView):
    pass


class CreateBlogView(views.CreateView):
    pass
