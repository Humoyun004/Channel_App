from django.urls import path

from .views import channel,home

urlpatterns = [
    path('', home, name='home'),
    path('channel/', channel, name='channel'),
]