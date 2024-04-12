from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from Filmes.models import Filme, Avaliacao
from .serializers import  AvaliacaoSerializer ,AvaliacaoUpdateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Avg



class CreateReviewMovie(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):

        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
 
            user = request.user   #pega o usuario logado

            filme = Filme.objects.filter(id=request.data["filme"])

            if not filme.exists():
                return Response({"message": "Filme não encontrado"}, status=status.HTTP_404_NOT_FOUND)

            comentario = request.data["comentario"]

            nota = request.data["nota"]

            avaliacao = Avaliacao(filme=filme.first(), usuario=user, comentario=comentario, nota=nota)
            avaliacao.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


class UpdateReviewMovie(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request,avaliacaoid):
        serializer = AvaliacaoUpdateSerializer(data=request.data)
        avaliacao = Avaliacao.objects.filter(id=avaliacaoid , usuario=request.user)
        if not avaliacao.exists():
                print("Avaliação não encontrada")
                return Response({"message": "Avaliação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            comentario_atual = Avaliacao.objects.get(id=avaliacaoid).comentario
            nota_atual = Avaliacao.objects.get(id=avaliacaoid).nota

            #se nao for passado comentario ou nota, mantem o que ja estava
            if "comentario" not in request.data:
                request.data["comentario"] = comentario_atual
            if "nota" not in request.data:
                request.data["nota"] = nota_atual
                

            avaliacao=Avaliacao.objects.filter(id=avaliacaoid).update(nota=request.data["nota"], comentario=request.data["comentario"])
            print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListReviewMovie(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request , filmeid):
        filme_id = filmeid
        if filme_id is not None:
            filme = Filme.objects.filter(id=filme_id)
            if not filme.exists():
                return Response({"message": "Filme não encontrado"}, status=status.HTTP_404_NOT_FOUND)
            avaliacoes = Avaliacao.objects.filter(filme=filme.first())
            #coloca as avaliacoes em um dicionario
            resultado = []
            for avaliacao in avaliacoes:
                 resultado.append({"usuario": avaliacao.usuario.username, "comentario": avaliacao.comentario, "nota": avaliacao.nota})

            return Response({'avaliacoes':resultado}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "ID do filme não fornecido"}, status=status.HTTP_400_BAD_REQUEST)

    

class DeleteReviewMovie(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, avaliacaoid):
        avaliacao = Avaliacao.objects.filter(id=avaliacaoid)
        if not avaliacao.exists():
            return Response({"message": "Avaliação não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        avaliacao.delete()
        return Response({"message": "Avaliação deletada"}, status=status.HTTP_200_OK)



class ListActorsMovie(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        filme = Filme.objects.filter(id=request.data["filme"])
        if not filme.exists():
            return Response({"message": "Filme não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        atores = filme.first().atores.all()
        atores = atores.values()
        return Response(atores, status=status.HTTP_200_OK)
    

#lista todos os filmes com seus nomes e ids
class ListMovies(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        filmes = Filme.objects.all()
        filmes = filmes.values('id', 'titulo')
        return Response(filmes, status=status.HTTP_200_OK)
    
    
