# WebScraping utilizando o framework da botcity
## Visão Geral
Esse projeto contém o script de automação para fazer uma coleta de dados de um site utilizando o framework BotCity
### Estrutura do Projeto
* dados_ibge: Contém a estrutura do projeto.<br>
* src/models: Contém o código fonte da requisição a API do IBGE onde nos retorna o nome dos estados.<br>
* src/services: Contém o código fonte da criação da planilha Excel utilizando a biblioteca pandas.<br>
* bot.py: Contém o código fonte com a lógica completa da automação.

### Requisitos do Sistema
* Python 3.12.0.
* Biblioteca pandas.
* Biblioteca requests.

### Instalação
* Instale usando "pip install -r requirements.txt".

### Observação
* Este script de automação só pode ser totalmente automatizado com todas as bibliotecas e frameworks instalados corretamente. 
* Nesse código a API utilizada é pública.
* Certifique-se de que o arquivo "chromedriver.exe" esteja na mesma versão que o seu browser.
* Rode o projeto utilizando "python bot.py".
