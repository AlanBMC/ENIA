from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('paginas/<int:id_pagina>', views.pagina, name='paginas'),
    path('registro/', views.registro, name='registro'),
]
