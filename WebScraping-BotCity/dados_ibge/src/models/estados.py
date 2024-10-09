import requests

def estados():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

    response = requests.get(url)
    response_json = response.json()

    estados = []

    if response.status_code == 200:
        for estado in response_json:
            nome = estado["nome"]
            estados.append(nome)
            
        return estados
    else:    
        return(f"Erro {response.status_code} na api de estados:{response.text}")