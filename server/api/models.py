from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome_completo = models.CharField(max_length=150, null=False)
    contato = models.IntegerField(null=False)
    secao = models.IntegerField(null=False,max_length=3)
    cadeiras = models.IntegerField(null=False,max_length=3)
    filme = models.CharField(null=False)

    def __str__(self):
        return self.nome_completo