import requests
from openpyxl import Workbook
from openpyxl.styles import Font
from design import estilo_celulas

#API IBGE
url_ibge = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

resposta_url = requests.get(url_ibge)

#Status da API
api_status = resposta_url.status_code

#criar arquivo excel
workbook = Workbook()
planilha_dados =  workbook.active
planilha_dados.title = 'Dados dos estados do Brasil'

#função de estilo das celulas
estilo_celulas(planilha_dados)

#verificação se a api está online
if api_status == 200:
    api_json = resposta_url.json()
    qnt_estados = len(api_json)

    #Coleta de dados da API
    for estado in api_json:
        nome_estado = estado['nome']
        sigla_estado = estado['sigla']
        regiao_estado = estado['regiao']['nome']

        #Definir a posição das colunas e dos dados
        coluna_dados = ['A', 'B', 'C']
        dados_coletados = [nome_estado, sigla_estado, regiao_estado]
        fonte_dados = Font(size=12)

        #Determinar da posição na planilha
        interacao = planilha_dados.max_row + 1
        
        #Preencher a planilha com os dados
        for coluna_exata, dado_exato in zip(coluna_dados, dados_coletados):
            celula_exata = coluna_exata + str(interacao)
            planilha_dados[celula_exata].value = dado_exato
            planilha_dados[celula_exata].font = fonte_dados

        #Salva o arquivo do excel
        workbook.save('Dados.xlsx')

else:
    #Tratativa de erro na API do IBGE
    print(f'A API do IBGE não está funcionando! {resposta_url.status_code}')
