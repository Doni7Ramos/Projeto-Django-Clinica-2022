# O módulo views é responsável por conter todas as funções que retornam informações ao usuário
# Para isso também será necessário receber as requisições

from django.http import HttpResponse

# Por definição as funções de visualização precisam obrigatoriamente ter um parâmetro de request

def medicos (request):
    # Já o retorno será uma resposta HTTP, para isso será necessário utilizar a função HttpResponse

    return HttpResponse ('Esta é a página de Médicos')
    