import smtplib


def send_email(to_list,subject, text_body):
	gmail_user = 'chasegrieves.skywater@gmail.com'
	gmail_password = 'Unicorn123!'

	sent_from = gmail_user


	email_text = """\
From: %s
To: %s
Subject: %s

%s""" % (sent_from, ", ".join(to_list), subject, text_body)

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(sent_from, to_list, email_text)
	server.close()

	print('Email sent!')


if __name__ == "__main__":
	to = ['chase.grieves@skywatertechnology.com','grieveschase@gmail.com']
	subject = "yeet"
	body = """\
	line1
	2
	3
	4
	5

	6

	7

	8
	"""
	send_email(to,subject, body)
	print('done')
