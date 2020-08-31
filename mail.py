import smtplib
import ssl

port = 465

password = "Lakshan1/"

smtp_server = "smtp.gmail.com"
sender_email = "pythonbot213@gmail.com"  # Enter your address
receiver_email = "sivalakshan724@gmail.com"  # Enter receiver address
message = "Price has hit your watchlist"

# create a secure SSL context

context = ssl.create_default_context()


def sendmail():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("pythonbot213@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
