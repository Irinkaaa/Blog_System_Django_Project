from django.urls import path
from Blog_System.blogs import views

urlpatterns = [
    path('', views.BlogsListView.as_view(), name='index')
]