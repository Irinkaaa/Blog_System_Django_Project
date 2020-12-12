from django.urls import path
from Blog_System.blogs import views

urlpatterns = [
    path('', views.BlogsListView.as_view(), name='index'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog details'),

    path('<int:pk>/<slug:slug>/', views.BlogDetailView.as_view(), name='blog details'),

    path('create', views.CreateBlogView.as_view(), name='blog create'),
]

