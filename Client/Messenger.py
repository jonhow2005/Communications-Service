import Client_Server
import threading
import Server_Controller
import E2E_Manager

def WriteId(userId, *args):
    idfile = open("Id.txt", "w")
    idfile.write(str(userId))
    message = "N-" + userId
    Client_Server.msgfunc(message)
    
    
def sendMessage(data ,*args):
    for arg in args:
        data = data + " "+ str(*args)
    print(data)
    message,recipient = data.rsplit(" ", 1) 
    message = "M-" + message +"|"+ recipient
    Client_Server.msgfunc(message)
    
def sendKey(recipient,*args):
    with open("Key.txt", "r") as file:
        Key = file.read()
    message = "K-" + Key +"||"+ recipient
    Client_Server.msgfunc(message)

def recvKey(sender, key,*args):
    with open(f'Key/{sender}.txt', "w") as file:
        file.write(key)

def pushMessage(message, sender,*args):
    Server_Controller.globalmessage = "cmd# " + message + " " + sender 
    Server_Controller.sendbool = True
    
def sendE2E(keyid, message, recipient,*args):
    message = E2E_Manager.Encrypt(keyid, message)
    message = "E-" + message +"|"+ recipient
    Client_Server.msgfunc(message)
      
def receiveE2E(message, sender,*args):
    message = E2E_Manager.Decrypt(message)
    pushMessage(message, sender)
