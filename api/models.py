from django.db import models

# Create your models here.
# 88996106494
class Cadastro (models.Model):
    nome_completo = models.CharField(max_length=150,null=False)
    contato = models.IntegerField(null=False,primary_key=True)
    filme = models.CharField(max_length=150,null=False)
    secao = models.IntegerField(null=False)
    cadeira = models.IntegerField(null=False)

    def __str__(self):
        return self.nome_completo
    

