import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print 'Script demonstrates How To send emails using Python'
print '==================================================='
print ''

yLogin = "yourLogin"
yPassword = "yourPassword"

server = smtplib.SMTP('smtp.mail.yahoo.com') #smtp,port number
server.ehlo()
server.starttls()
server.ehlo()

server.login (yLogin,yPassword)

fromaddr = "youremail@yahoo.com"
toaddr = "youremail@yahoo.com"
subject = "From Python"


msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject

body = "Sent from Python"

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

print 'message sent'
