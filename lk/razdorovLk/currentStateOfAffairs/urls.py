from django.contrib.auth import views,urls
from django.urls import path
from .views import AffairsPage

urlpatterns = [
    path('', AffairsPage.as_view(), name='affairs'),  # Страница Состояния дела
]
