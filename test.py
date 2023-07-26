#Code that sends out the email (put this in a if statement when the window is up)

from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

credentials_File = 'credientials.json' #This is the file generated by google, it's basically the API key for the email
gmail = 'gmail'  #API type
version = 'v1'
scope = ['https://mail.google.com/']

service = Create_Service(credentials_File, gmail, version, scope)

label_body = { #Labels if we decide to add them
'removeLabelIds': ['IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'],
'addLabelIds': ['Label_3']
}

def getEmails (): #Test 4 my list of my emails ---CHANGE THIS
    emails = ['jadasardin@gmail.com', 'jsardin@umich.edu']
    return emails


emailMsg = 'You Have a Maintenance Window Scheduled'
mimeMessage = MIMEMultipart()
for items in getEmails():
    mimeMessage['to'] = items
mimeMessage['subject'] = 'Maintenance Window'
mimeMessage.attach(MIMEText(emailMsg, 'plain'))

raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
#print(message)