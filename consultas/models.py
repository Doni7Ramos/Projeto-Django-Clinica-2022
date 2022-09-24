from django.db import models

# O modelo (models) trata-se de uma classe que estende models.Model
# Este modelo já possui divérsos recursos para o uso de banco de dados e 
#    interface, como o atributo id, que cria um identificador único para o
#    registro e objects, que trata do módulo manage que nos possibilita criar
#    comandos de consulta no banco de dados

# Documentação para selecionar os fields 
#  https://docs.djangoproject.com/en/4.1/ref/models/fields/

class Especialidade (models.Model):
    # Foi definido que o código da especialidade poderá ser somente números inteiros positivos, para isso foi utilizado o PositiveIntegerField.

    # CODIGO
    # AutoField (primary_key=True)
    codigo = models.PositiveIntegerField ()

    # NOME
    nome = models.CharField (
        max_length=255
    )

    # DESCRIÇÃO
    descricao = models.CharField (
        max_length=1000,
        null=True,
        blank=True
    )
    def __str__ (self):
        return self.nome



class Medico(models.Model):
    # Charfield: este tipo de atributo cria no banco de dados um campo de texto(VARCHAR)
    #  -É obrigatorio a parametrização do maximo de caracteres, para isso utilizamos o max_lenght.

    #Nome
    nome = models.CharField(
        max_length=255
        )

    # Por padrão não são aceitas informações nulas, para que não seja obrigatório o uso de determinado atributo é utilizado o parâmetro null para que no banco de dados seja um NOT NULL e blank para permitir informações em branco na interface

    #CPF
    cpf = models.CharField(
        max_length=11,
        null=True,
        blank=True
    )

    #CRM
    crm = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    #Datefield: tipo de atributo que representa uma data
    #DATA DE NASCIMENTO
    data_nascimento = models.DateField(
        null=True,
        blank=True
    )

    #CIDADE
    cidade = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    # EmailField: é o tipo que representa a estrutura de um e-mail.
    # Para o banco de dados é simplesmente um texto e para a interface é um componente com validação de e-mail.
    #E-MAIL
    email = models.EmailField(
        null=True,
        blank=True
    )

    # Dentro dos tipos disponibilizados pelo ModelFields (é possível localizar o tipo ForeignKey (chave estrangeira)), sendo assim o próprio Django se responsabiliza em estruturar o modelo de dados
    especialidade = models.ForeignKey (
        Especialidade,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    ) 


# Função padrão de classe para transformar uma classe em texto
    def __str__ (self):
        return self.nome
    
class Procedimento (models.Model):
    
    # Código
    codigo = models.PositiveIntegerField ()

    # Nome
    nome = models.CharField (
        max_length=255
    )

    # Descrição
    descricao = models.CharField (
        max_length=1000,
        null=True,
        blank=True
    )

    def __str__ (self):
        return self.nome