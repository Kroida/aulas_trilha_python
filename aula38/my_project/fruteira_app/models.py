from django.db import models

# Create your models here.

class Fruta(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Fruta'
        verbose_name_plural = 'Frutas'
