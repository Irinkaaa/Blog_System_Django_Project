from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog_System.blogs.urls')),
    path('auth/', include('Blog_System.authentication.urls')),
    path('api/blogs/', include('Blog_System.blogs_api.urls')),
]
