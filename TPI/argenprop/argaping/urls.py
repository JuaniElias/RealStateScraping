from django.urls import path
from django.views.static import serve
from django.conf import settings

from . import views

app_name = 'argaping'
urlpatterns = [
    path('', views.index, name='index'),
    path('Barrios_de_Rosario.geojson', serve, {
        'document_root': settings.STATICFILES_DIRS[0] + '/argaping/data/',
        'path': 'Barrios_de_Rosario.geojson'
    }),

]
