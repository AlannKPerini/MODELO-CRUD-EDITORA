from unittest.util import _MAX_LENGTH
from django.db import models
# criação das classes

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    cpf = models.PositiveIntegerField()
    endereco = models.CharField(max_length=255)
    email = models.EmailField()
    sexo = models.CharField(max_length=2)

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)

class Formato(models.Model):
    nome = models.CharField(max_length=255)

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    formato = models.ForeignKey(Formato, on_delete=models.CASCADE)
    data_lancamento = models.DateField()
    isbn = models.CharField(max_length=255)
    numero_paginas = models.PositiveIntegerField()

class aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro= models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor = models.DecimalField
    data = models.DateField()
