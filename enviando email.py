from email.message import EmailMessage
import ssl
import smtplib
meu_email = "kaianbig@gmail.com" # seu email aqui
senha_gerada = "22132213k" #sua senha aqui ou gere uma no email
destinatario_email = "kaian.freitas@hotmail.com" # email do destinatario
assunto = "testando" # assunto aqui
body = """"""
#teste
"""""" # mensagem do email
em = EmailMessage()

em["from"] = meu_email
em["to"] = destinatario_email
em["subject"] = assunto
em.set_content(body)

context = ssl.create_default_context() # criando om contexto ssl seguro

# smtp é o protocolo que permite enviar emails pela internet
# fazendo conexao com o servidor smtp do gmail usando ssl
with smtplib.SMTP_SSL('smtp.gmail.com' , 465, context = context) as smtp:
    smtp.login(meu_email, senha_gerada ) #fazendo o seu login
    smtp.sendmail(meu_email, destinatario_email, 
                  em.as_string()) # enviando email

