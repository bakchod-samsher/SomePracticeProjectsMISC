import smtplib, ssl

"""SAMPLE mail sending application using TLS or transport layer security"""


port = 587 #PORT NUMBER

password = input("ENTER PASSWORD")

sender_mail = "ENTER_THE_SENDER_MAIL"
reciever_mail = "ENTER_THE_RECIEVER_MAIL"

message = """HELLO I AM SENDING THIS MAIL FROM A PYTHON APPLICATION"""

with smtplib.SMTP("smtp.gmail.com",port) as server:
    server.starttls()
    server.login(sender_mail,password)
    server.sendmail(sender_mail,reciever_mail,message)
