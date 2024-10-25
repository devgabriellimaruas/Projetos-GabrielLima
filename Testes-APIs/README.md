# Test Automation
## Visão Geral
Esse projeto contém o script de automação para saber se uma API está funcionando corretamente e fazer o envio do seu status por e-mail.
### Estrutura do Projeto
* Test Automation: Contém o código-fonte da automação.<br>
* main.py: Ponto de entrada para a execução do robô.<br>
* statuscode.py: Contém o código para obter o status da API.

### Requisitos do Sistema
* Python 3.12.0.
* Biblioteca requests.

### Instalação
* Instale usando "pip install smtplib".
* Instale usando "pip install requests".

### Observação
* Este script de automação só pode ser totalmente automatizado se a aplicação de destino possuir uma API em nuvem acessível. 
* Certifique-se de que a API está configurada corretamente e disponível para garantir o funcionamento adequado do robô RPA. 
* Consulte a documentação da API para obter informações sobre autenticação e endpoints necessários.
* Nesse código a API utilizada é pública.
