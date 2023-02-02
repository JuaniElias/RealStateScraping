from django.urls import path

from . import views

app_name = 'argaping'
urlpatterns = [
    path('', views.index, name='index'),
]
