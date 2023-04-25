from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.nome
    

class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150, null=True,blank=True)
    telefone = models.CharField(max_length=15, unique=True )
    email = models.EmailField(blank=True, null=True, unique=True)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('nome', 'sobrenome', 'id')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'