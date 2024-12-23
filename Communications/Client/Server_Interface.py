import Ip_Finder
import E2E_Manager
import Messenger
import ChatManager
import KeyFinder
import ContactManager

commands = [Ip_Finder.Getip, # 0
            Ip_Finder.ReadId, 
            Ip_Finder.WriteId, 
            E2E_Manager.GenerateKey,
            Messenger.sendMessage,
            Messenger.pushMessage, # 5
            Messenger.sendKey,
            KeyFinder.Findkey,      
            Messenger.sendE2E,
            Messenger.receiveE2E,
            E2E_Manager.Decrypt, # 10
            E2E_Manager.Encrypt, 
            ContactManager.GetContacts,
            ChatManager.GrabConvo,
            ContactManager.GetGC,
            ContactManager.GetPrivs]

def receiveCommand(command):
    return sendCommand(*command.split(" ", 2))

def sendCommand(command, *args):
    output = None
    output = commands[int(str(command))](*args)
    print(output)
    if output != None:
        output = str(command) + " " + str(output)
    return output
