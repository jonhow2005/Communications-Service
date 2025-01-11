import Client_Server
import threading
import Server_Controller
import E2E_Manager

def WriteId(userId, *args):
    idfile = open("Data/Id.txt", "w")
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
    with open("Data/Key.txt", "r") as file:
        Key = file.read()
    message = "K-" + Key +"||"+ recipient
    Client_Server.msgfunc(message)
    
#"a+" simply fails for some reason
def recvKey(sender, key,*args):
    with open('privateChats.txt', "a") as file:
        file.write(" "+ sender)
        file.close()
    with open('privateChats.txt', "r") as file:
        x = file.read().split(" ").index(sender)
        file.close()
    with open(f'Data/keys/{x}.txt', "w") as keyfile:
        keyfile.write(key)
        keyfile.close()
        
def pushMessage(message, sender,*args):
    Server_Controller.globalmessage = "cmd# " + message + " " + sender 
    Server_Controller.sendbool = True
        
def sendE2E(keyid, message,*args):
    print(f'Key #{keyid}')
    recipient = open(f'Data/privateChats.txt', "r").read().split(" ")[int(keyid)]
    with open(f'Data/Chats/Priv/{recipient}',  'a') as file:
            file.write(f'\n You: {message}\n')
            file.close()
    message = E2E_Manager.Encrypt(keyid, message)
    message = "E-" + message + "|" + recipient
    Client_Server.msgfunc(message)   
def receiveE2E(message, sender,*args):
    message = E2E_Manager.Decrypt(message)
    with open(f'Data/Chats/Priv/{sender}', 'a') as file:
            file.write(f'\n {sender}: {message}\n')
            file.close()