from django.urls import path
from Blog_System.blogs_api.views import CreatePostApiView

urlpatterns = [
    path('', CreatePostApiView.as_view(), name='post create api')
]
