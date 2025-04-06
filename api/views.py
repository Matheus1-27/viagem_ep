from django.shortcuts import render
from .models import Cadastro
# Create your views here.

def formulario(request):
    if request.method == 'POST':
        novo_cadastro = Cadastro()
        novo_cadastro.nome_completo = request.POST.get("nome") 
        novo_cadastro.contato  = request.POST.get("fone")
        novo_cadastro.filme = request.POST.get("filme")
        novo_cadastro.secao = int(request.POST.get("secao"))
        novo_cadastro.cadeira = request.POST.get("cadeira")
        novo_cadastro.save()
        return render(request, "index.html")
    else:
        return render(request, "index.html")
        