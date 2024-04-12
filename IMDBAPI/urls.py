from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from usuarios.views import UserCreateAPIView
from Filmes.views import CreateReviewMovie , ListReviewMovie, ListActorsMovie , ListMovies , UpdateReviewMovie , DeleteReviewMovie
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.obtain_auth_token),#Responsavel por validar o meu username e password e me retornar um token
    path('register/', UserCreateAPIView.as_view()),
    path('review/', CreateReviewMovie.as_view()),
    #passa o id do filme no listreview
    path('reviews/<int:filmeid>/', ListReviewMovie.as_view()),
    path('listactors/', ListActorsMovie.as_view()),
    path('listmovies/', ListMovies.as_view()),
    path('avaliacao/<int:avaliacaoid>/update/', UpdateReviewMovie.as_view()),
    path('avaliacao/<int:avaliacaoid>/delete/', DeleteReviewMovie.as_view(), name='delete_review'),
    
]
