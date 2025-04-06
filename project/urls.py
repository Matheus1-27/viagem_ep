from django.contrib import admin
from django.urls import path,include
from api.views import formulario
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',formulario, name='Cadastro')
]
