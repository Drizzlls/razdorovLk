from django.contrib.auth import views,urls
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy
from .views import RegisterPage, LoginPage, PasswordResetPage, EmailVeirfy, LogoutViewPage, ProfilePage
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('', ProfilePage.as_view(), name='profile'),

    # Аккаунт
    path('login/', LoginPage.as_view(), name='login'),  # Вход в аккаунт
    path('employees/logout/', LogoutViewPage.as_view(), name='logout'),  # Выход из аккаунта

    # Регистрация
    path('register/', RegisterPage.as_view(), name='register'),  # Регистрация пользователя
    path('register/confirm_email/',
         TemplateView.as_view(template_name='registration/confirm_email.html'),
         name='confirm_email'),  # Страница с текстом о подтверждении регистарции
    path('register/verify_email/<uidb64>/<token>/',
         EmailVeirfy.as_view(), name='verify_email'), # Страница с токеном после подтверждения регистрации
    path('register/verify_email/invalid_verify/',
         TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'),  # Страница с токеном после подтверждения регистрации

    # Сброс пароля
    path('password_reset/', PasswordResetPage.as_view(), name='password_reset'),  # Сброс пароля
    path('password_reset/password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # Сообщение об оправки письма на почту при сбросе пароля
    path('password_reset/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Ввод нового пароля
    path('password_reset/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # Сообщение о смене пароля
]
