from django.urls import path

from . import views

urlpatterns = [
    path('', views.on_event, name='on_event'),
]
