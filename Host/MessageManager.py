bufferIndex = []
bufferCheck = []
barrier = "]|-=-|["
import socket
import time
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
    #V2 Update: dict
    global bufferIndex
    global bufferCheck
    z = 0
    y = bufferCheck[z]
    print(f'async:{bufferIndex}')
    for x in bufferCheck:
        if z in bufferIndex:
            pass
        else:
            return bufferCheck[x]
        z=z+1
    
def theMethod(sender,data):
    inst,data = data.split("-")
    if inst   == "M":
        handleMessage(f'{data}|{sender}', inst)
    elif inst == "K":
        handleMessage(f'{data}||{UserManager.findUser(sender)}', inst)
    elif inst == "N":
        UserManager.newUser(data, sender)   
    if inst   == "E":
        handleMessage(f'{data}|{sender}', inst)
        
def handleMessage(data,type):
    if type == "K":
        message,recipient,sender = data.split("||")
    else:
        message,recipient,sender = data.split("|")
    try:
        with open(f'Chats/{recipient}', "r") as file:
            file.close()
        print("error: try continues after error")
        logChat(UserManager.findUser(sender), recipient, message)
    except:    
        queueMessage(type ,sender, message, UserManager.findIP(recipient))

def queueMessage(type, sender, message, recipient):
    global barrier
    global bufferIndex
    abc = checkBuffer()
    print(checkBuffer())
    with open(f'Send Buffer/{abc}', "w") as file:
        file.write(f'{type}{barrier}{sender}{barrier}{recipient}{barrier}{message}')
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
def clearBuffer(ipaddress, socket, rRt):
    while True:
        time.sleep(2)
        findkey(UserManager.findUser(ipaddress), socket)
        for x in bufferIndex:
            print("Check")
            f = open(f'Send Buffer/{x}', "r")
            i,r,r2,m = f.read().split(barrier)
            print(i, r, r, m)
            f.close()
            if checkClient(r) == 0 or checkClient(r2) == 0:
                if r != ipaddress and r2 != ipaddress:
                    return
            if r2 == ipaddress:
                if i == "E":
                    socket.send(f'5 {m} {UserManager.findUser(r)}'.encode())
                if i == "M":
                    socket.send(f'18 {UserManager.findUser(r)} {UserManager.findUser(r)}: {m}'.encode())
                if i == "K":
                    socket.send(f'20 {UserManager.findUser(r)} {m}'.encode())
            if r == ipaddress:
                if i == "M":
                    socket.send(f'18 {UserManager.findUser(r2)} You: {m}'.encode())
            bufferIndex.remove(x) 
        