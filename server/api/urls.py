from django.urls import path
from .views import get_cadastros,create_cadastros

urlpatterns =[ 
    path("",get_cadastros, name='coleta_cadastro'),
    path("create_cadastro/",create_cadastros, name='create_cadastro')
]
