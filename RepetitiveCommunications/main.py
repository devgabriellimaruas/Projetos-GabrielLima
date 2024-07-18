import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import openpyxl
from arquivoexcel import Criar_Arquivo

#Configurações do servidor SMTP e credenciais
smtplib_server = 'smtp.seudominio.com'
smtplib_port = 1 #Substituir o 1 por uma porta no formato int
smtplib_username = 'Seu email'
smtplib_password = 'Sua senha'

#Destinatário e informações do e-mail
destinatario = 'Email do destinatario'
assunto = 'Assunto do email'

#Criando arquivo excel
Criar_Arquivo()

#Ler dados do arquivo Excel
def ler_dados_excel(arquivo_excel):
    abrir_excel = openpyxl.load_workbook(arquivo_excel)
    planilha = abrir_excel.active
    dados = []

    for linha in planilha.iter_rows(min_row=2, values_only=True):
        nome, idade, email = linha
        dados.append(f'Nome: {nome}, Idade: {idade}, E-mail: {email}')

    return '\n'.join(dados)

#Criar o objeto MIMEMultipart para o e-mail
mensagem = MIMEMultipart()
mensagem['From'] = smtplib_username
mensagem['To'] = destinatario
mensagem['Subject'] = assunto

#Ler dados do arquivo Excel e adicioná-los ao corpo do e-mail
dados_excel = ler_dados_excel('dados.xlsx')
texto = f'Dados do Excel:\n{dados_excel}'

#Adicionar o corpo do e-mail em formato de texto
mensagem.attach(MIMEText(texto, 'plain'))

try:
    #Configurar a conexão SMTP
    server = smtplib.SMTP(smtplib_server, smtplib_port)
    server.starttls()
    server.login(smtplib_username, smtplib_password)

    #Enviar o e-mail
    server.sendmail(smtplib_username, destinatario, mensagem.as_string())
    print(f'E-mail enviado com sucesso para {destinatario}: {assunto}')

    #Fechar a conexão SMTP
    server.quit()

except Exception as e:
    print(f'Erro ao enviar e-mail: {str(e)}')