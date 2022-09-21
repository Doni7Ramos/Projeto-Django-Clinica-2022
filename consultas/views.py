# O módulo views é responsável por conter todas as funções que retornam informações ao usuário
# Para isso também será necessário receber as requisições
<<<<<<< HEAD

# O Django inclui no código das views por padrão a importação do django.shortcuts.render
# Este módulo é responsável por transformar o template em um html legível para o navegador

from django.shortcuts import render

from .models import Especialidade, Medico
=======

from django.http import HttpResponse
>>>>>>> 5a8024efa53b4b6901137251c9772bea3f5e84f2

# Por definição as funções de visualização precisam obrigatoriamente ter um parâmetro de request

def medicos (request):
<<<<<<< HEAD
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

    contexto2 = {'especialidades': especialidades}

    return render (request, 'especialidades.html', contexto2)
=======
    # Já o retorno será uma resposta HTTP, para isso será necessário utilizar a função HttpResponse

    return HttpResponse ('Esta é a página de Médicos')
>>>>>>> 5a8024efa53b4b6901137251c9772bea3f5e84f2
    