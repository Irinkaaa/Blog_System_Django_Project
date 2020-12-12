from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Blog_System.authentication.forms import SignUpForm, SignInForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class SignInView(LoginView):
    template_name = "auth/signin.html"
    form_class = SignInForm


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')
