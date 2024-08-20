from django.contrib.auth import views,urls
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView
from .views import TasksPage

urlpatterns = [
    path('', TasksPage.as_view(), name='tasks'),

]
