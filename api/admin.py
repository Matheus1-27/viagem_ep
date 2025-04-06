from django.contrib import admin
from .models import Cadastro
# Register your models here.

cadastrados = {
    'Cadastrados': Cadastro.objects.all()
}

