from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
from . import views


app_name = 'argaping'
urlpatterns = [
    path('', views.index, name='index'),
]
