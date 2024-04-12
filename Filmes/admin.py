from django.contrib import admin

# Register your models here.

from Filmes.models import Filme, Avaliacao , Ator, Diretor, Genero, rel_filme_ator, rel_filme_genero


admin.site.register(Filme)

admin.site.register(Avaliacao)

admin.site.register(Ator)

admin.site.register(Diretor)

admin.site.register(Genero)

admin.site.register(rel_filme_ator)

admin.site.register(rel_filme_genero)
