from django.contrib.auth import views,urls
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from .views import ShopPage, ShopHistoryPage, ShopHandler

urlpatterns = [
    path('', ShopPage.as_view(), name='shop'),
    path('history/', ShopHistoryPage.as_view(), name='history'),
    path('handler/', ShopHandler.as_view(), name='handler'),

]
