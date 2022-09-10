from django.urls import path

from . import views

urlpatterns = [
    # ex: /abm/
    path('', views.index, name='index'),
    # ex: /abm/5/alta/
    path('<int:id_socio>/alta', views.alta, name='alta'),
    # ex: /abm/5/baja/
    path('<int:id_socio>/baja/', views.baja, name='baja'),
    # ex: /abm/5/modificacion/
    path('<int:id_socio>/modificacion/', views.modificacion, name='modificacion'),
]
