import email_sender

def askForEmailandPassword():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")
    return email,password,name

def askForRecepients():
    recepients = []
    numOfRecepients = int(input("Please input number of recepient(s): "))
    for i in range(numOfRecepients): 
        recepients.append(input(f"Email Recepient No.{i+1}: "))
    return recepients

def confirmation(email,recepients,name):
    print(f"\nHello, {name}!")
    print(f"Your email is {email}")
    print(f"Your recepient(s) are: {recepients}")
    return input("\nIs this final? (Y/N) ")

while(True):
    email,password,name = askForEmailandPassword()
    recepients = askForRecepients()
    confirm = confirmation(email,recepients,name)
    if(confirm=="Y" or confirm=="y"):
        break
    else:
        pass

subject = input("\nPlease enter subject: ")
message = input("\nPlease enter your message: ")

for recepient in recepients:
    email_sender.sendMessage(name,recepient,subject,message,email,password)
print("\nMessage sent!")




