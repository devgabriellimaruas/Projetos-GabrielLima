import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from statuscode import status_code

status_code()

def Mensageria():
    #Configurações do servidor SMTP e credenciais
    smtplib_server = 'smtp.seudominio.com'
    smtplib_port = 1 #Substituir o 1 por uma porta no formato int
    smtplib_username = 'Seu email'
    smtplib_password = 'Sua senha'

    #Destinatário e informações do e-mail
    destinatario = 'Email do destinatario'
    assunto = 'Assunto do email'

    #Criar o objeto MIMEMultipart para o e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = smtplib_username
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    texto = status_code()

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
