import socket
#V2 Update store data in dict
#V2 username Data overwrite frome server if already chosen. (IP locked accounts)

def Getip(*args):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    ipfile = open("Data/Html/Ip_File.html", "w")
    #V2 Update: Integrate More
    ipfile.write(f"<!DOCTYPE html> \n \n<html lang=\"en\">\n <head> \n <meta charset=\"utf-8\" /> \n <title>IP ADDRESS</title> \n <link rel= \" stylesheet \" href=\"styles.css\"/> \n </head> \n <body id = 'ip'> \n{ip_address}\n </body>")
    ipfile.close()    
    
def pushId(userId, *args):
    idfile = open("Data/Id.txt", "w")
    if userId != "None":
        idfile.write(str(userId))
    
def ReadId(*args):
    try:
        idfile = open("Data/Id.txt", "r")
        userId = idfile.read()
    except:
        userId = ""
    return userId

