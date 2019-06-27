import smtplib
from email.mime.text import MIMEText

def sendEmail(item, link, category):
	print("sending email meow")
	user = "EMAIL ADDRESS"
	pw = "PASSWORD"

	msg = MIMEText(item + "\n\n" + \
	"Check /r/buildapcsales for more information: \n\n" + \
	link)

	msg['Subject'] = category.capitalize() + " for sale!"
	msg['From'] = user
	msg['To'] = user

	server = smtplib.SMTP_SSL('smtp.gmail.com')
	server.ehlo()
	server.login(user, pw)
	server.sendmail(user, user, msg.as_string())
	server.close()
