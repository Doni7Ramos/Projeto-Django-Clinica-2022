# O arquivo urls.py é responsável por tratar o direcionamento das rotas conforme a requisição do usuário.

from django.urls import path

from . import views

# Variável obrigatória
# A variável urlpatterns é uma lista e a ordem dos itens importam
urlpatterns = [
    # A função path é responsável por estruturar a rota da aplicação
    path('', views.medicos),
    path('medicos/', views.medicos),
    path('especialidades/', views.especialidades)
]