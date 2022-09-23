# O módulo views é responsável por conter todas as funções que retornam informações ao usuário
# Para isso também será necessário receber as requisições

from django.shortcuts import render

##from django.http import HttpResponse

from .models import Medico, Procedimento


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

# Função desenvolvida para fornecer os detalhes do medico, para isso foi necessário que fosse declarado o parâmetro medico_id para receber a informação vinda da URL

def medico_detalhes (request, medico_id):

    # Para todos os modelos é possível utilizar o método get que tem a função de fazer uma consulta no banco de dados e retornar somente um item

    # pk é um parâmetro possível que faz referência à pimary key (chave primária) definida no modelo

    medico = Medico.objects.get(pk=medico_id)

    contexto = { 'medico': medico }

    return render(request, 'medico_detalhes.html', contexto)

def procedimentos(request):

    procedimentos = Procedimento.objects.all()

    contexto = {'procedimentos' : procedimentos }

    return render (request, 'procedimentos.html', contexto)

def procedimentos_detalhes (request, codigo):

    procedimento = Procedimento.objects.get(pk=codigo)

    contexto = { 'procedimento' : procedimento}

    return render (request, 'procedimento_detalhes.html', contexto)



    