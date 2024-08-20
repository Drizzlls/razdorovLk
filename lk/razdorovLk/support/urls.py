from django.contrib.auth import views,urls
from django.urls import path
from .views import SupportPage

urlpatterns = [
    path('', SupportPage.as_view(), name='support'),  # Страница поддержки
]
