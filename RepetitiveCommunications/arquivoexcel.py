import openpyxl

def Criar_Arquivo():
    #Criar um novo arquivo Excel
    arquivo_excel = openpyxl.Workbook()

    #Selecionar a planilha ativa
    dados = arquivo_excel.active

    #Adicionar cabeçalho a planilha
    dados['A1'] = 'Nome'
    dados['B1'] = 'Idade'
    dados['C1'] = 'E-mail'

    #Adicionar dados a planilha
    dados_lista = [
        ('João', 30, 'joao@email.com'),
        ('Maria', 25, 'maria@email.com'),
        ('Pedro', 35, 'pedro@email.com'),
        ('Ana', 28, 'ana@email.com')
    ]

    #Loop for para iterar os elementos da lista no arquivo
    for linha, (nome, idade, email) in  enumerate(dados_lista, start=2):
        dados[f'A{linha}'] = nome
        dados[f'B{linha}'] = idade
        dados[f'C{linha}'] = email

    #Salvar o arquivo Excel
    arquivo_excel.save('dados.xlsx')

    return 'Arquivo criado com sucesso!'