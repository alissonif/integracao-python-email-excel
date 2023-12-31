import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd

gerentes_df = pd.read_excel('Enviar E-mails.xlsx')
# gerentes_df.info()
for i, email in enumerate(gerentes_df['E-mail']):
  gerente = gerentes_df.loc[i, 'Gerente']
  area = gerentes_df.loc[i, 'Relatório']
  # Configurações do servidor SMTP do Outlook.com
  outlook_smtp_server = 'smtp.office365.com'
  outlook_smtp_port = 587

  # Informações de autenticação
  username = 'seu_email@outlook.com'
  password = 'sua_senha'

  # Criar uma mensagem de email
  msg = MIMEMultipart()
  msg['From'] = username
  msg['To'] = 'seu_email@gmail.com'  # Substitua pelo endereço do destinatário
  msg['Subject'] = 'Relatório de {}'.format(area)

  # Corpo da mensagem
  mensagem = '''
  Presado {},
  Segue em anexo o Relatório {}, conforme solicitado.
  Qualquer dúvida estou à disposição.
  Att.,
'''.format(gerente, area)
  msg.attach(MIMEText(mensagem, 'plain'))

  # Anexar um arquivo
  with open('{}.xlsx'.format(area), 'rb') as file:
      attachment = MIMEApplication(file.read(), _subtype="txt")
  attachment.add_header('Content-Disposition', 'attachment', filename='{}.xlsx'.format(area))
  msg.attach(attachment)

  # Estabelecer conexão com o servidor SMTP
  server = smtplib.SMTP(outlook_smtp_server, outlook_smtp_port)
  server.starttls()  # Use STARTTLS para criptografia

  # Faça login na conta do Outlook.com
  server.login(username, password)

  # Envie o email
  email = 'seu_email@gmail.com'  # Substitua pelo endereço do destinatário
  server.sendmail(username, email, msg.as_string())

  # Encerre a conexão com o servidor SMTP
  server.quit()
