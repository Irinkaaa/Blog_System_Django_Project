from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic as views
from Blog_System.blogs.models import Blog
from Blog_System.common.utils import can_user_create_blogs


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

    def dispatch(self, request, *args, **kwargs):
        if not can_user_create_blogs(request.user):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
