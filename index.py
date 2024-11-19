import requests
import smtplib
#used for sending plain text mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

def check_website(url):
      try:
           response = requests.get(url)
           if response.status_code == 200 :
                  #website is up
                  return True
           else: 
                return False
      except:
              return False

def send_email(sender_email,receiver_email,password,subject,body):
         message = MIMEMultipart()
         message["From"] = sender_email
         message["To"] = receiver_email
         message["Subject"] = subject
         message.attach(MIMEText(body,"plain"))
      
         try :
             server = smtplib.SMTP('smtp.gmail.com',587)
             server.starttls() #start  connection
             server.login(sender_email,password)
             text = message.as_string()
             server.sendmail(sender_email,receiver_email,text)
             server.quit() #close connection
             print("Email sent sucessfully")

         except :
              print("Failed to send an email")
url = "https://fakestoreapi.org/"
if not check_website(url):
         sender_email = os.getenv("sender_email")
         receiver_email = os.getenv("receiver_email")
         password = os.getenv("password")
         subject = "website is not working"
         body = "the application is in terminated state"
         send_email(sender_email,receiver_email,password,subject,body)
else:
    print("website is up")
