from django.db import models

# Create your models here.
from usuarios.models import Usuario


#definir como sera chamdo no admin no plural
class Diretor(models.Model):#criar tabelas de 
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    bio = models.TextField()
    foto = models.URLField()

    class Meta:
        verbose_name_plural = "Diretores"



    def __str__(self):
        return self.nome
class Genero(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Generos"

    def __str__(self):
        return f'Genero {self.nome}'

class Ator(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    bio = models.TextField()
    foto = models.URLField()

    class Meta:
        verbose_name_plural = "Atores"

    def __str__(self):
        return self.nome
    




class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano = models.IntegerField()
    duracao = models.IntegerField()
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    sinopse = models.TextField()
    poster = models.URLField()

    class Meta:
        verbose_name_plural = "Filmes"

    def __str__(self):
        return self.titulo
    
class rel_filme_ator(models.Model):#tabela intermediaria
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)# um para muitos
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Relacoes filmes e atores"

    def __str__(self):
        return self.filme.titulo + " - " + self.ator.nome
    
class rel_filme_genero(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Relacoes filmes e generos"

    def __str__(self):
        return self.filme.titulo + " - " + self.genero.nome

class Avaliacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True , null=True)


    class Meta:
        verbose_name_plural = "Avaliacoes"

    def __str__(self):
        return self.filme.titulo
    


    

