from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Админка
    path('', include('account.urls')), # Страница Профиля
    path('shop/', include('shop.urls')), # Страница Магазина
    path('tasks/', include('tasks.urls')), # Страница Задач
    path('support/', include('support.urls')), # Страница Поддержки
    path('affairs/', include('currentStateOfAffairs.urls')), # Страница Состояния дела
    path('api/', include('api.urls')), # Страница Состояния дела
]
