import imaplib, email
from email.policy import default
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
 
user = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
imap_url = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imap_url)
 
con.login(user, password)
con.select(mailbox='INBOX', readonly=False)

typ, data = con.search(None, 'ALL')

def parse_email(email_bytes: bytes) -> dict:
    """
    Parse email data from bytes to extract sender, subject, date, and body.

    Args:
        email_bytes (bytes): Email data in bytes format.

    Returns:
        dict: Dictionary containing parsed email information.
    """
    msg = email.message_from_bytes(email_bytes, policy=default)

    sender = msg['From']

    subject = msg['Subject']

    date = msg['Date']
    body = ""
    if msg.is_multipart():
        for part in msg.get_payload():
            if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = msg.get_payload(decode=True).decode()
    
    sender = sender.split('<')
    sender_name = sender[0]
    sender_email = sender[1].split('>')[0]

    email_dict = {
    'Sender': sender_name,
    'Email': sender_email,
    'Subject': subject,
    'Date': date,
    'Body': body
    }
    return email_dict

all_data = []

for num in data[0].split()[:50]:
    typ, em_data = con.fetch(num, '(RFC822)')
    data = parse_email(em_data[0][1])
    all_data.append(data)


df = pd.DataFrame(all_data)
print(df.head())
df.to_csv('email.csv',index=False)