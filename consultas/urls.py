# O arquivo urls.py é responsável por tratar o direcionamento das rotas conforme a requisição do usuário.

from django.urls import path

from . import views

# Variável obrigatória
# A variável urlpatterns é uma lista e a ordem dos itens importam
urlpatterns = [
    # A função path é responsável por estruturar a rota da aplicação
    path('', views.medicos),
    path('medicos/', views.medicos),
    # Para criar uma url dinâmica é necessário colocar a parte dinâmica entre < e > , o valor associado nesta parte da URL será passado por parâmetro para a view
    # O Django fará a seguinte chamada de função para este exemplo
    ## views.medico_detalhes(request=request, medico_id=medico_id)
    path('medico/<medico_id>/detalhes/', views.medico_detalhes, name='medico_detalhes'),
    path('procedimentos/', views.procedimentos),
    path('procedimento/<codigo>/detalhes/', views.procedimentos_detalhes, name='procedimento_detalhes'),
]