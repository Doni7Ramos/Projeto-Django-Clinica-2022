# O módulo views é responsável por conter todas as funções que retornam informações ao usuário
# Para isso também será necessário receber as requisições

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from .models import Medico, Procedimento, Especialidade, Consulta


# Por definição as funções de visualização precisam obrigatoriamente ter um parâmetro de request

def index (request):

    return render (request, 'index.html')

def especialidades (request):

    especialidades = Especialidade.objects.all()

    contexto = {'especialidades': especialidades}

    return render(request, 'especialidades.html', contexto)

def especialidade_detalhes (request, codigo):

    especialidade = Especialidade.objects.get(pk=codigo)

    contexto = { 'especialidade' : especialidade}

    return render (request, 'especialidade_detalhes.html', contexto)

def especialidade_cadastro (request):
    if request.POST:

        nome = request.POST['nome']

        descricao = request.POST['descricao']

        procedimento = Especialidade(
            nome = nome,
            descricao = descricao
        )

        procedimento.save()

        return HttpResponseRedirect (reverse('especialidades'))

    return render(request, 'especialidade_cadastro.html' )    

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

def medico_detalhes (request, codigo):

    # Para todos os modelos é possível utilizar o método get que tem a função de fazer uma consulta no banco de dados e retornar somente um item

    # pk é um parâmetro possível que faz referência à pimary key (chave primária) definida no modelo

    medico = Medico.objects.get(pk=codigo)

    contexto = { 'medico': medico }

    return render(request, 'medico_detalhes.html', contexto)

def medico_cadastro (request):
    
    especialidades = Especialidade.objects.all()

    contexto = {'especialidades': especialidades} 

    if request.POST:

        nome = request.POST['nome']

        email = request.POST['txt_email']

        cpf = request.POST['txt_cpf']
        
        crm = request.POST['txt_crm']

        data_nascimento = request.POST['txt_data'] if request.POST['txt_data'] != "" else None

        cidade = request.POST['txt_cidade']

        uf = request.POST['txt_uf']

        especialidade_codigo = request.POST['especialidade']

        especialidade = Especialidade.objects.get(codigo=especialidade_codigo)

        medico = Medico(
            nome=nome,
            email=email,
            especialidade=especialidade,
            cpf=cpf,
            crm=crm,
            data_nascimento=data_nascimento,
            cidade=cidade,
            uf=uf
            )
        
        medico.save()

        return HttpResponseRedirect (reverse('medicos'))

    return render(request, 'medico_cadastro.html', contexto)

def procedimentos(request):

    procedimentos = Procedimento.objects.all()

    contexto = {'procedimentos' : procedimentos }

    return render (request, 'procedimentos.html', contexto)

def procedimento_detalhes (request, codigo):

    procedimento = Procedimento.objects.get(pk=codigo)

    contexto = { 'procedimento' : procedimento}

    return render (request, 'procedimento_detalhes.html', contexto)

def procedimento_cadastro (request):
    if request.POST:

        nome = request.POST['nome']

        descricao = request.POST['descricao']

        procedimento = Procedimento(
            nome = nome,
            descricao = descricao
        )

        procedimento.save()

        return HttpResponseRedirect (reverse('procedimentos'))

    return render(request, 'procedimento_cadastro.html' )  

def consultas (request):

    consultas = Consulta.objects.all()

    contexto = {'consultas': consultas}

    return render (request, 'consultas.html', contexto)

def consulta_detalhes (request, codigo):

    consulta = Consulta.objects.get(pk=codigo)

    procedimentos = consulta.procedimento.all()

    contexto = {
        'consulta' : consulta,
        'procedimentos' : procedimentos
        }

    return render (request, 'consulta_detalhes.html', contexto)

def consulta_cadastro (request):

    medicos = Medico.objects.all()

    procedimentos = Procedimento.objects.all()

    contexto = {
        'medicos': medicos,
        'procedimentos': procedimentos
    }

    if request.POST:

        data = request.POST['data']

        codigo_medico = request.POST['medico']

        medico = Medico.objects.get(pk=codigo_medico)

        laudo = request.POST['laudo']

        consulta = Consulta(
            data = data,
            medico = medico,
            laudo = laudo
        )

        consulta.save()

        procedimentos_lista = request.POST.getlist('procedimentos')

        for procedimento in procedimentos_lista:

            procedimento_listado = Procedimento.objects.get(pk=procedimento)
            
            consulta.procedimento.add(
                procedimento_listado
            )

            consulta.save()
        
        return HttpResponseRedirect (reverse('consultas'))
    
    return render(request, 'consulta_cadastro.html', contexto)