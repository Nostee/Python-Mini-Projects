import smtplib
from email.message import EmailMessage

def sendMessage(name,recepient,subject,message,email_account,password):
    email = EmailMessage()
    email["from"] = name
    email["to"] = recepient
    email["subject"] = subject

    email.set_content(message)

    with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()                              
        smtp.starttls()                          
        smtp.login("nosteeeeeee@gmail.com","Jedidiah1") 
        smtp.send_message(email)  
    
    return("All done!")


