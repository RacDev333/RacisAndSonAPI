import os
import resend
from dotenv import load_dotenv

from email_templates import get_contact_confirmation_html

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")


def send_email_to_client(address: str, name: str):

    content = get_contact_confirmation_html(name)

    try:
        params = {
            "from": "Racis&Son <kontakt@racis.store>", 
            "to": [address],
            "subject": "Dziękujemy za kontakt!",
            "html": content,
        }

        email = resend.Emails.send(params)
        return email
    except Exception as e:
        print(f"Błąd wysyłki: {e}")
        return None

def send_email_to_team(address: str, name: str, message: str):

    content = f"Dostałeś nową wiadomość od: {name} \nEmail: {address} \nTreść: {message}"

    try:
        params = {
            "from": "Racis&Son <info@racis.store>", 
            "to": "kontakt@racis.store",
            "subject": f"Nowa wiadomość od: {name}",
            "html": content,
        }

        email = resend.Emails.send(params)
        return email
    except Exception as e:
        print(f"Błąd wysyłki: {e}")
        return None

def send_email(address: str, name: str, message: str):
    send_email_to_team(address, name, message)
    send_email_to_client(address, name)



def order_confirmation_email(address: str, name: str, order_num: str):

    content = f"Cześć {name}! \nTwoje zamówienie {order_num} zostało przyjęte i oczekuje na realizację. \n\nDziękujemy za zaufanie, \nZespół Racis&Son"

    try:
        params = {
            "from": "Racis&Son <kontakt@racis.store>", 
            "to": [address],
            "subject": "Zamówienie przyjęte!",
            "html": content,
        }

        email = resend.Emails.send(params)
        return email
    except Exception as e:
        print(f"Błąd wysyłki: {e}")
        return None