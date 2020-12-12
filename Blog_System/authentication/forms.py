from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Blog_System.common.form_mixins import BootstrapFormMixin


class SignUpForm(BootstrapFormMixin, UserCreationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()


class SignInForm(BootstrapFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()
