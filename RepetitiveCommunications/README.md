# Repetitive Communications
## Visão Geral
Esse projeto contém o script de automação para enviar emails a partir de um arquivo excel.
### Estrutura do Projeto
* Repetitive Communications: Contém o código-fonte da automação.<br>
* main.py: Ponto de entrada para a execução do robô.<br>
* arquivoexcel.py: Contém o código para criar o documento excel, caso seja necessário.
* dados.xlsx: É o arquivo excel pré-criado.

### Requisitos do Sistema
* Python 3.12.0.
* Biblioteca smtplib.
* Biblioteca openpyxl.

### Instalação
* Instale usando "pip install smtplib".
* Instale usando "pip install openpyxl".

### Observação
* Este script de automação só pode ser totalmente automatizado se a aplicação de destino possuir uma API em nuvem acessível. 
* Certifique-se de que a API está configurada corretamente e disponível para garantir o funcionamento adequado do robô RPA. 
* Consulte a documentação da API para obter informações sobre autenticação e endpoints necessários.
