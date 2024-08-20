from django.contrib.auth import views,urls
from django.urls import path, include, reverse_lazy
from api.views import UpdateDeal

urlpatterns = [
    path('update-deal/', UpdateDeal.as_view(), name='update-deal'),

]
