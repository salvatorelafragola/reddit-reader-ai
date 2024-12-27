import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List


class EmailSender:
    def __init__(
        self,
        smtp_server: str,
        port: int,
        email: str,
        username: str,
        password: str
    ):
        """
         Inizializza l'oggetto EmailSender con le credenziali SMTP.

         :param smtp_server: Indirizzo del server SMTP.
         :param port: Porta del server SMTP.
         :param email: Indirizzo mail del mittente
         :param username: Nome utente per l'autenticazione SMTP.
         :param password: Password per l'autenticazione SMTP.
         """
        self.smtp_server = smtp_server
        self.port = port
        self.email = email
        self.username = username
        self.password = password

    def send_mail(self,
                  to: List[str],
                  subject: str,
                  body: str,
                  is_html: bool = False
                  ) -> bool:
        """
        Invia un'email con il soggetto, il corpo e i destinatari specificati.

        :param to: Lista di destinatari principali.
        :param subject: Soggetto dell'email.
        :param body: Corpo dell'email.
        :param is_html: Indica se il corpo è in formato HTML. Predefinito False.
        :return: True se l'invio ha avuto successo, False altrimenti.
        """

        # Composizione del messaggio
        message = MIMEMultipart()
        message["From"] = f"<{self.email}>"
        message["To"] = ", ".join(to)
        message["Subject"] = subject

        # Specifica il formato del messaggio (HTML o plain text)
        mime_type = "html" if is_html else "plain"
        message.attach(MIMEText(body, mime_type))

        try:
            # Connessione al server SMTP
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Abilita crittografia TLS
                server.login(self.username, self.password)
                server.sendmail(self.email, to, message.as_string())
            print("Email inviata con successo.")
            return True
        except Exception as e:
            print(f"Errore durante l'invio dell'email: {e}")
            return False

