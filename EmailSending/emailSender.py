import smtplib  # simple mail transfer protocol
from string import Template
from pathlib import Path  # os.path similar
from email.message import EmailMessage


html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = "Piyush Mahapatra"
email['to'] = 'piyushmahapatra001@gmail.com'
email['subject'] = 'Hello Gorgeous'

email.set_content(html.substitute({'name': 'PiyushsuperTramp'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # password is hidden for obvious Reason
    smtp.login('socialbeenoreply@gmail.com', 'appm2020')
    smtp.send_message(email)
    print("All good Boss!")
