from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import ShopItem
from coins.models import History
from account.models import User
from django.shortcuts import get_object_or_404
from coins.shop import CoinsForShop
from integrations.bitrix.Lead import Lead


class ShopPage(View):
    """ Страница регистрации """
    template_name = 'shop/index.html'

    def get(self, request):
        context = {
            'items': ShopItem.objects.all()
        }
        return render(request, self.template_name, context=context)

class ShopHistoryPage(View):
    """ Страница регистрации """
    template_name = 'shop/history.html'

    def get(self, request):
        context = {
            'itemsHistory': History.objects.filter(user=request.user)
        }

        return render(request, self.template_name, context=context)

class ShopHandler(View):
    """ Обработчик покупок """
    def post(self, request):
        coins = CoinsForShop(user=request.user, idItem=request.POST['item'])
        coins.minusCoins()
        return redirect(request.META.get('HTTP_REFERER'))
