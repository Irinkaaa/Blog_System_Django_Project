from django.urls import path
from .views import SignInView, SignUpView, SignOutView

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
]

from .receivers import *
