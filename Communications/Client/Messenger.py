import Client_Server
import threading
import Server_Controller
import E2E_Manager

def sendMessage(message, recipient):
    message = "M-" + message +"|"+ recipient
    thread = threading.Thread(target=Client_Server.msgfunc, args = str(message))
    thread.start
    thread.join
    
def sendKey(Key, recipient):
    message = "K-" + Key +"|"+ recipient
    thread = threading.Thread(target=Client_Server.msgfunc, args = str(message))
    thread.start
    thread.join

def pushMessage(message, sender):
    Server_Controller.globalmessage = message + " " + sender 
    Server_Controller.sendbool = True
    
def sendE2E(keyid, message, recipient):
    message = E2E_Manager.Encrypt(keyid + message)
    message = "E-" + message +"|"+ recipient
    thread = threading.Thread(target=Client_Server.msgfunc, args = str(message))
    thread.start
    thread.join
    Client_Server.msgfunc(message)
      
def receiveE2E(message, sender):
    message = E2E_Manager.Decrypt(message)
    message = message + " " + sender
    pushMessage(message)
