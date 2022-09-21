# clinica-2022

Projeto do curso de Django

A porposta deste projeto é construir uma aplicação web para atender uma clinica.

O objetivo é desenvolver as seguintes telas:

- Médicos
- Especialidades
- Procedimentos
- Consultas

## Preparar o ambiente

1. Instalação do venv 

````
python -m venv venv
````

2. Ativar o ambiente virtual (venv)

````
.\venv\Scripts\activate
````

3. Instalação do Django

````
pip install django
````

## Estruturação do Projeto

1. Criar o Projeto

NOTE: Projeto é o local que o motor do Django é executado, com isso as configurações são feitas dentro dele, utilizando o arquivo settings.py

````
django-admin startproject clinica .
````

- django-admin: É o comando de terminal responsável pela administração do Django

    - startproject: Parâmetro do comando django-admin responsável por estruturar um projeto em Django
        
        É obrigatório informar o nome do projeto (neste caso clinica).
        Como próximo parâmetro é o diretório que será estruturado o projeto, que a sujestão é informar o caminho relativo do diretório local " ." 

### Iniciar o serviço Web

````
python -m manage runserver
````

- manage: Módulo do Django responsável por executar ações dentro do projeto
    - runserver: Parâmetro que determina a execução do módulo Web disponível dentro do Django para desenvolvimento

O site estará disponivel do endereço http://127.0.0.1:8000/

2. Criar um APP

NOTE: O APP (aplicação) será o local no Django que será implementada toda a lógica. Lembrando que um projeto pode ter vários APPs.

````
python -m manage startapp consultas
````

clinica: pasta que contem os arquivos do projeto
consultas: pasta que trata os arquivos da aplicação

## Adicionando o APP ao Projeto

É necessário entrar no arquivo settings.py e localizar a constante INSTALLED_APPS.
A constante INSTALLED_APPS é uma lista que contém todos os APPs associados ao projeto, somente após um APP estar relacionado nesta lista que o Django pode identificar e utilizar o APP nos demais fins

IMPORTANTE: Configurar o TIME_ZONE para que a aplicação seja executado com o horário local.

> https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Configurar o linguagem da aplicação no 
> LANGUAGE_CODE http://www.i18nguy.com/unicode/language-identifiers.html

````
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
````

## Registrar o APP à aplicação admin

A aplicação admin é uma interface gerada de maneira automática pelo Django que utiliza o modelo desenvolvido na aplicação para criar uma interface básica de gestão, ou seja, uma tela de lista, detalhes, inclusão, atualização e exclusão. 

C -> Create (Criar)
R -> Read (Ler)
U -> Update (Atualizar)
D -> Delete (Excluir)

Para registrar a aplicação é necessário localizar o arquivo consultas/admin.py e incluir os comandos de registro do modelo.

### Cadastrar SuperUsuario

Para acessar a tela de admin é necessario que se tenha um usuario devidamente registrado na aplicação

````
python -m manage createsuperuser
````

# Migration 

O migration (migrações) é o ato de capturar o modelo de dados desenvolvido em uma camada de aplicação, e preparar os códigos necessários para criar o banco de dados.

> IMPORTANTE: o migrate não está vinculado a nenhum banco de dados específico

````
python -m makemigrations consultas
````

- **makemigrations**: é o comando responsável pela preparação do modelo que será implantado no banco de dados

    - Como parâmetro é necessário informar o nome da aplicação

Após a execução deste comando, a pasta migrations é criada dentro da aplicação (Consultas/Migrations).

````
python -m manage migrate consultas
````

-**migrate**: é o comando responsável por aplicar a estrutura criada pelo makemigrations

## URLconf

A URLconf é o termo utilizado para fazer tratar os arquivos url.py. Este arquivo está presente no projeto e na aplicação.

O comando startapp não cria o arquivo urls.py na aplicação. É necessário criar o arquivo.

<<<<<<< HEAD
> IMPORTANTE: o arquivo deve conter obrigatoriamente uma variável chamada urlpatterns

=======
> IMPORTANTE: o arquivo deve conter obrigatoriamente uma variável chamada urlpatterns
>>>>>>> 5a8024efa53b4b6901137251c9772bea3f5e84f2
