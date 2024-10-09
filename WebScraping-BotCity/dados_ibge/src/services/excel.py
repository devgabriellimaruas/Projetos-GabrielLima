import pandas as pd

def tratar_dados(item):
    return {k: v.replace('\n', '').replace(',', '.').title() for k, v in item.items()}

def excel(dados):
    dados_tratados = [tratar_dados(item) for item in dados]
    df = pd.DataFrame(dados_tratados)
    df.to_excel("Coleta de dados IBGE.xlsx", index=False)
    return "Planilha criada com sucesso"
