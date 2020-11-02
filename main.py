from gmail_adapter import GmailAdapter
from messages import WelcomeMessage
#zmienne środowiskowe
from dotenv import load_dotenv
from os import getenv

load_dotenv()

mailer = GmailAdapter(
    host= 'smtp.gmail.com',
    port= 465,
    username= getenv("player"),
    password= getenv("haslo")
)

mailer.login()

welcome = WelcomeMessage()

mailer.send_mail(
    recipient_email="greg139@wp.pl",
    subject='hello',
    content=welcome.render(name='Grzegorz'))
