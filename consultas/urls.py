# O arquivo urls.py é responsável por tratar o direcionamento das rotas conforme a requisição do usuário.

from django.urls import path

from . import views

# Variável obrigatória
# A variável urlpatterns é uma lista e a ordem dos itens importam
urlpatterns = [
    # A função path é responsável por estruturar a rota da aplicação
    # Para criar uma url dinâmica é necessário colocar a parte dinâmica entre < e > , o valor associado nesta parte da URL será passado por parâmetro para a view
    # O Django fará a seguinte chamada de função para este exemplo
    ## views.medico_detalhes(request=request, medico_id=medico_id)

    path('', views.index, name='index'),
    path('medicos/', views.medicos, name='medicos'),
    path('medicos/cadastro/', views.medico_cadastro, name='medico_cadastro'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('especialidades/cadastro/', views.especialidade_cadastro, name='especialidade_cadastro'),
    path('procedimentos/', views.procedimentos, name='procedimentos'),
    path('procedimentos/cadastro/', views.procedimento_cadastro, name='procedimento_cadastro'),
    path('consultas/', views.consultas, name='consultas'),
    path('consultas/cadastro', views.consulta_cadastro, name='consulta_cadastro'),

    path('medicos/<codigo>/detalhes/', views.medico_detalhes, name='medico_detalhes'),
    path('procedimentos/<codigo>/detalhes/', views.procedimento_detalhes, name='procedimento_detalhes'),
    path('especialidades/<codigo>/detalhes/', views.especialidade_detalhes, name='especialidade_detalhes'),
    path('consultas/<codigo>/detalhes/', views.consulta_detalhes, name='consulta_detalhes'),
]