import requests


def status_code():
    url_ibge = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    response_url = requests.get(url_ibge)
    status_url = response_url.status_code
    return status_url
