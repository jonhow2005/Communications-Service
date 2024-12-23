import socket

def Getip(*args):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    ipfile = open("Ip_File.html", "w")
    ipfile.write(f"<!DOCTYPE html> \n \n<html lang=\"en\">\n <head> \n <meta charset=\"utf-8\" /> \n <title>IP ADDRESS</title> \n <link rel= \" stylesheet \" href=\"styles.css\"/> \n </head> \n <body id = 'ip'> \n <div id = 'ip'>{ip_address} </div> \n </body>")
    ipfile.close()
    
def WriteId(userId, *args):
    idfile = open("Id.txt", "w")
    idfile.write(str(userId))
    
def ReadId(*args):
    idfile = open("Id.txt", "r")
    userId = idfile.read()
    return userId

