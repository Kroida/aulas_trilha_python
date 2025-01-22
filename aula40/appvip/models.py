from django.db import models
from datetime import date

# Create your models here.

class Socio(models.Model):
    TIPO_CHOICES = [
        ('titular', 'Titular'),
    ]
    
    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    tipo_socio = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descricao = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome_completo
    
    @property
    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        if hoje.month < self.data_nascimento.month or (hoje.month == self.data_nascimento.month and hoje.day < self.data_nascimento.day):
            idade -= 1
        return idade
