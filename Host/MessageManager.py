bufferIndex = []
bufferCheck = []
barrier = "]|-=-|["
import socket
import UserManager
targetSocket = ''
def onStart(buffersize):
    global bufferIndex
    global bufferCheck
    y = 0
    for x in range(0,int(buffersize)):
        bufferCheck.append(y)
        y = y+1
    
def checkBuffer():
    print("check")
    #V2 Update: dict
    global bufferIndex
    global bufferCheck
    z = 0
    y = bufferCheck[z]
    print(bufferIndex)
    for x in bufferCheck:
        if z in bufferIndex:
            pass
        else:
            return bufferCheck[x]
        z=z+1
    
def theMethod(sender,data):
    inst,data = data.split("-")
    if inst == "M":
        handleMessage(f'{data}|{sender}')
    elif inst == "K":
        handleKey(f'{data}||{UserManager.findUser(sender)}')
    elif inst == "N":
        UserManager.newUser(data, sender)
          
def handleMessage(data):
    message,recipient,sender = data.split("|")
    try:
        with open(f'Chats/{recipient}', "r") as file:
            file.close()
        logChat(UserManager.findUser(sender), recipient, message)
    except:    
        queueMessage(sender, message, UserManager.findIP(recipient))

def handleKey(data):
    message,recipient,sender = data.split("||")
    global barrier
    sender = UserManager.findIP(sender)
    recipient = UserManager.findIP(recipient)
    with open(f'KeyBuffer/{recipient}.txt', "w") as file:
        file.write(f'{sender}{barrier}{message}')
        file.close()
              
def queueMessage(sender, message, recipient):
    global barrier
    global bufferIndex
    abc = checkBuffer()
    print(checkBuffer())
    with open(f'Send Buffer/{abc}', "w") as file:
        file.write(f'{sender}{barrier}{recipient}{barrier}{message}')
    bufferIndex.append(abc)

def findkey(user, socket):
    global barrier
    try:
        with open(f'KeyBuffer/{user}.txt', "w") as file:
            x,y = file.read().split(barrier)
        socket.send(f'20 {x} {y}')  
    except:
        pass    
     
def logChat(sender, chat, message):
    with open(f'Chats/{chat}') as file:
        file.write(f'{sender}: {message}')
        file.close()
        
def checkClient(ipaddress):
    return UserManager.check(ipaddress)
                           
#V2 Send Message despite offline User
def clearBuffer(ipaddress, socket):
    findkey(UserManager.findUser(ipaddress), socket)
    
    for x in bufferIndex:
        f = open(f'Send Buffer/{x}', "r")
        r,r2,m = f.read().split(barrier)
        if (checkClient(r) == 0 | checkClient(r2) == 0) | r !=ipaddress & r2 != ipaddress:
            return
        if r2 == ipaddress:  
            socket.send(f'18 {UserManager.findUser(r)} {UserManager.findUser(r)}: {m}'.encode())
        if r == ipaddress:  
            socket.send(f'18 {UserManager.findUser(r2)} You: {m}'.encode())
        bufferIndex.remove(x) 
        f.close()
        