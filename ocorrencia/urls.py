from django.urls import path
from . import views

urlpatterns = [
    path('<int:ano>', views.index, name='index'),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('envolvido/', views.cadastro, name='envolvido'),
    path('alerta/', views.alertas, name='alerta'),
    path('graficos/', views.graficos, name='graficos'),
 ]