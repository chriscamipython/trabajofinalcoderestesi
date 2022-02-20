from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('', views.vendedores, name="Vendedores"),
    path('', views.objetos, name="Objetos"),
    path('', views.lugar, name="Lugares"),
    path('', views.compradores, name="Compradores"),
]
