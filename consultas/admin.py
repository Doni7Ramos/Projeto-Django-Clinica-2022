from django.contrib import admin

#Importar o módulo criado dentro do arquivo models.py, sendo assim é necessário a utilização do .models visto que models é o nome do módulo e o "."(ponto) é a estrutura do pacote (package)

from .models import Consulta, Medico, Especialidade, Procedimento

# O registro é feito através do modulo contrib, preveamente importado pelo Django
# Para acontecer o registro é necessário dentro do atributo "site" executar o método "register", passando por parâmetro o modelo, para este caso Medico

admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(Procedimento)
admin.site.register(Consulta)