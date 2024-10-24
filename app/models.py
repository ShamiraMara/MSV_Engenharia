from django.db import models

# Create your models here.

class Atendimento(models.Model):
    nome = models.CharField(max_length=100, verbose_name= "")
    tipo = models.CharField(max_length=100, verbose_name= "Tipo de planta")
    dimensoes = models.CharField(max_length=100, verbose_name= "Dimensões ultilizadas")
    materiais = models.CharField(max_length=100, verbose_name= "Materiais ultilizados")
    descricao = models.CharField(max_length=100, verbose_name= "Descrição sobre a planta")
    preco = models.CharField(max_length=100, verbose_name= "Valor da planta")
   
    def __str__(self):
        return f"{self.nome}, {self.tipo}, {self.dimensoes}, {self.materiais}, {self.descricao}, {self.preco}"
    class Meta:
        verbose_name =  "Atendimento"
        verbose_name_plural = "Atendimentos"

class GaleriaDePlanta(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "")
    descricao = models.CharField(max_length=100, verbose_name = "")
    imagem = models.CharField(max_length=100, verbose_name = "")

    def __atr__(self):
        return f"{self.nome}, {self.descricao}, {self.imagem}"
    class Meta:
        verbose_name = "GaleriaDePlanta"
        verbose_name_plural = "GaleriDePlantas"

class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name= "")
    telefone = models.CharField(max_length=100, verbose_name= "")
    cidade = models.CharField(max_length=100, verbose_name= "")
    email = models.CharField(max_length=100, verbose_name= "")
    senha = models.CharField(max_length=100, verbose_name= "")

    def __str__(self):
        return f"{self.nome}, {self.telefone}, {self.cidade}, {self.email}, {self.senha}"
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural ="Usuarios"