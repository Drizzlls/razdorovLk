from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationForm,
                                       AuthenticationForm as DjangoAuthenticationForm,
                                       PasswordResetForm as DjangoPasswordResetForm,
                                       SetPasswordForm as DjangoPasswordResetConfirmView)
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .utils import send_email_for_verify


User = get_user_model()


class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(
        label=('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','class': 'input', 'placeholder':'youremail@mail.ru',
                                       'type': 'email', 'autofocus': 'false'})
    )
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'type':'password',
                                                              'placeholder':'Введите пароль'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'type':'password',
                                                              'placeholder':'Повторите пароль'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'Иванов'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Иванович'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'+ 7 999 999 99 99'}))

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'surname', 'phone')

class AuthenticationForm(DjangoAuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={"autofocus": True, 'class': 'input' ,
                                                               'placeholder':'Ваш Email', 'type': 'email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'input','type':'password',
                                                             'placeholder':'Введите пароль'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )

            if self.user_cache is None:
                print(self.get_invalid_login_error())
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Email не верефицирован. Проверьте свою почту.',
                    code='invalid_login',
                )

        return self.cleaned_data


class PasswordResetForm(DjangoPasswordResetForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={'autocomplete': 'email', "autofocus": True, 'class': 'input', 'placeholder': 'Ваш Email',
                   'type': 'email'})
    )

class PasswordResetConfirmForm(DjangoPasswordResetConfirmView):
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'input','type':'password',  'placeholder':'Введите пароль'}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'input','type':'password',  'placeholder':'Повторите пароль'}))

