from django.urls import path

from . import views

app_name = 'one-country-a-day'
urlpatterns = [path("", views.index, name='index')]
