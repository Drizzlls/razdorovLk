from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
# from bitrixData.views import Bitrix24Api
# from .forms import UserCreationForm, PasswordResetForm
from .forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
# from .forms import AuthenticationForm, PasswordResetConfirmForm
# from .utils import send_email_for_verify
from .utils import send_email_for_verify
from integrations.bitrix.Lead import Lead
from integrations.bitrix.Deal import Deal
from .tasks import createAfterRegistrationTask

User = get_user_model()

class RegisterPage(View):
    """ Страница регистрации """
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        idDeal = request.GET.get('utm_source', 'Нет')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            if idDeal.isdigit():
                print('Ютм соурс есть', idDeal)
                ### FIXME: кинуть в целери
                createAfterRegistrationTask(id=idDeal, user=user)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class LoginPage(LoginView):
    """ Страница входа в аккаунт """
    form_class = AuthenticationForm

class PasswordResetPage(PasswordResetView):
    """ Страница сброса пароля """
    form_class = PasswordResetForm


class EmailVeirfy(View):
    """ Подтверждение почты """
    LeadInBitrix24 = Lead()
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            if request.GET.get('source',0):
                print('Есть ')
            ### FIXME: Кинуть в целери
            add = self.LeadInBitrix24.add(user=user, data={'TITLE': 'Регистрация в личном кабинете'})
            user.idLeadFromBitrix24 = add
            user.save()
            login(request, user)
            return redirect('login')
        return redirect('invalid_verify')

    # Находим юзера
    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, user.DoesNotExist, ValidationError):
            user = None
        return user

class LogoutViewPage(LoginRequiredMixin,View):
    """ Выход из аккаунта """
    login_url = 'login'

    def get(self, request):
        logout(request)
        return redirect('login')

class ProfilePage(LoginRequiredMixin,View):
    """ Страница профиля """
    template_name = 'account/profile.html'
    login_url = 'login'

    def get(self, request):
        return render(request, self.template_name)
