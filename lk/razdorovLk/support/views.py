from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import SupportForm
from .saveApplication import Application


class SupportPage(LoginRequiredMixin,View, Application):
    """ Страница поддержки """
    template_name = 'support/index.html'
    login_url = 'login'

    def get(self, request):
        context = {
            'form': SupportForm
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        userform = SupportForm(request.POST)
        if userform.is_valid():
            self.saveApplication(userform=userform, request=request)
        else:
            print('Форма невалидна!')
        return redirect(request.META.get('HTTP_REFERER'))