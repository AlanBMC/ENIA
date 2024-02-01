from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('nova_pagina/<int:id_pagina>/<str:username>', views.pagina, name='nova_pagina'),
    path('salvar_texto/', views.salva_texto, name='salva_texto'),
]
