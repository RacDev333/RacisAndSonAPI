import smtplib
from email.message import EmailMessage
import os
import resend
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

def send_email_to_client(address: str, name: str):

    content = f"Cześć {name}! \nDziękujemy za kontakt. Nasz zespół zajmie się twoją sprawą jak najszybciej. \nProsimy o cierpliwość – dołożymy wszelkich starań aby odpowiedzieć Ci jak najszybciej! \n\nDziękujemy za zaufanie, \nZespół Racis&Son"

    msg = EmailMessage()
    msg["From"] = "Racis&Son <twojmail@gmail.com>"
    msg["To"] = address
    msg["Subject"] = f"Dziękujemy za kontakt!"
    msg.set_content(content)

    with smtplib.SMTP(
        os.getenv("EMAIL_HOST"),
        int(os.getenv("EMAIL_PORT"))
    ) as server:
        server.starttls()
        server.login(
            os.getenv("EMAIL_USER"),
            os.getenv("EMAIL_PASSWORD")
        )
        server.send_message(msg)

def send_email_to_team(address: str, name: str, message: str):

    content = f"Dostałeś nową wiadomość od: {name} \nEmail: {address} \nTreść: {message}"

    msg = EmailMessage()
    msg["From"] = "Racis&Son <twojmail@gmail.com>"
    msg["To"] = os.getenv("EMAIL_USER")
    msg["Subject"] = f"Nowa wiadomość od: {name}"
    msg.set_content(content)

    with smtplib.SMTP(
        os.getenv("EMAIL_HOST"),
        int(os.getenv("EMAIL_PORT"))
    ) as server:
        server.starttls()
        server.login(
            os.getenv("EMAIL_USER"),
            os.getenv("EMAIL_PASSWORD")
        )
        server.send_message(msg)

def send_email(address: str, name: str, message: str):
    send_email_to_team(address, name, message)
    send_email_to_client(address, name)



def order_confirmation_email(address: str, name: str, order_num: str):

    content = f"Cześć {name}! \nTwoje zamówienie {order_num} zostało przyjęte i oczekuje na realizację. \n\nDziękujemy za zaufanie, \nZespół Racis&Son"

    msg = EmailMessage()
    msg["From"] = "Racis&Son <twojmail@gmail.com>"
    msg["To"] = address
    msg["Subject"] = f"Zamówienie przyjęte!"
    msg.set_content(content)

    with smtplib.SMTP(
        os.getenv("EMAIL_HOST"),
        int(os.getenv("EMAIL_PORT"))
    ) as server:
        server.starttls()
        server.login(
            os.getenv("EMAIL_USER"),
            os.getenv("EMAIL_PASSWORD")
        )
        server.send_message(msg)