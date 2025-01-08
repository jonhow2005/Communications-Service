from itertools import islice
datalog = []

def requestUser(ipaddress):
    with open("userdata", "r") as file:
        for line in file:
            if str(ipaddress) in line:
                return line.split("::-::",1)[1]
            
    
def newUser(username, ipaddres):
    ipaddres = str(ipaddres)
    #V2 Update: Use Dict
    with open("userdata", "a+") as file:
        for line in file:
            if line.find(str(ipaddres)) != -1:
                pass
            else:
                return "Already Registered"
        file.write(f'{ipaddres}::-::{username} \n')
        file.close()

def findIP(user):
    with open("userdata", "r") as file:
        for line in file:
            if line.find(user) != -1:
                return line.split("::-::", 1)[0]
        return "N/A"
            
def findUser(ipaddress):
    with open("userdata", "r") as file:
        for line in file:
            if line.find(str(ipaddress)) != -1:
                return line.split("::-::", 1)[1]
        return "N/A"                 
                 
def logData(data):
    global datalog
    datalog.append(data)
def delogData(data):
    global datalog
    datalog.remove(data)
def check(data):
    global datalog
    return datalog.count(data)