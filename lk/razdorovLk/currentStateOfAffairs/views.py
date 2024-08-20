from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Affairs


class AffairsPage(LoginRequiredMixin, View):
    """ Страница текущего положения дела """
    template_name = 'affairs/index.html'
    login_url = 'login'

    def get(self, request):
        if request.user.affair:
            return render(request, self.template_name)
        else:
            return redirect('profile')