from django.urls import path
from . import views

urlpatterns = [
    path('<int:ano>', views.index, name='index'),
    path('', views.index, name='index'),
 ]