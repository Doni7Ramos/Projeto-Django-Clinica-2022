# O módulo views é responsável por conter todas as funções que retornam informações ao usuário
# Para isso também será necessário receber as requisições

from django.shortcuts import render

from .models import Medico
from .models import Especialidade

# Por definição as funções de visualização precisam obrigatoriamente ter um parâmetro de request

def medicos (request):
    # Utilizar o modelo (para este caso Medico) para buscar do banco de dados
    medicos = Medico.objects.all()

    #variavel do tipo dicionário que será responsável por armazenar o contexto que será enviado para o template

    contexto = {'medicos': medicos}

    ### Já o retorno será uma resposta HTTP, para isso será necessário utilizar a função HttpResponse ###

    # Quando os módulos do shortcut são utilizados é simplificado é reduzido o volúme de código

    # No caso do render, é necessário colocar como primeiro parâmetro o request, em segundo o template e por último o contexto.

    return render(request, 'medicos.html', contexto)

def especialidades (request):

    especialidades = Especialidade.objects.all()

    contexto = {'especialidades': especialidades}

    return render (request, 'especialidades.html', contexto)
    