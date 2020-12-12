from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from Blog_System.blogs.models import Blog


class BlogsListView(views.ListView):
    template_name = 'blogs/list.html'
    model = Blog


class BlogDetailView(views.DetailView):
    template_name = 'blogs/details.html'
    model = Blog


class CreateBlogView(LoginRequiredMixin, views.CreateView):
    model = Blog
    template_name = 'blogs/create.html'
    fields = ('name', 'description')
