import random
keyarray = [0,0,0,0]

def GenerateKey(*args):
    keyarray[1] = int(1)
    keyarray[2] = int(1)
    r = int(random.randint(0,9))
    keyarray[0] = r
    rounds = int(126-32)
    keyarray[3] = int(1)
    polykey = (str(""))
    polyarray = []
    x = int(0)
    polyrand = int(random.randint(32,126))
    while x < rounds:
        while polyarray.count(polyrand) == 0:
            polyarray.append(polyrand)
            polykey = str(polykey + "|"+ str(polyrand))
            x = x+1    
        if polyarray.count(polyrand) != 0:
            if int(len(polyarray)) < int(99-32):
                polyrand = int(random.randint(32,99))
            else:
                polyrand = int(random.randint(32,126))
    keyarray.append(str(polykey))
    key = ""
    for x in keyarray:
        key = str(str(key) + str(x))
    with open("Key.txt", "w") as keyfile:
        keyfile.write(key)
    

def dekey(text,array):
    global keyarray
    xvar = int(0)
    while xvar < 3:
        for char in text: 
            array[xvar] = int(char)
            xvar = int(xvar) + 1
            if xvar == 4:
                break
    larray = text.split("|")
    for x in larray:
        if int(larray.index(x)) > 0:
            array.append(int(x))
    keyarray = array
    
def decryptreversal(message):
   versedmessage = str("")
   for char in message:
        versedmessage = str(char + versedmessage)
   return versedmessage

def deceasarcypher(message):
    r = int(keyarray[0])
    ceasarmessage = str("")
    for char in message:
        letter = ord(char)-r
        letter = chr(letter)
        ceasarmessage = str(ceasarmessage + letter)
    return(ceasarmessage)

def depolygraph(message):
    polymessage = str("")
    for char in str(message):
        letter = int(ord(char))
        letter = keyarray.index(letter)
        letter = chr(letter+32-4)
        polymessage = str(polymessage + letter)
    return(polymessage)


def Decrypt(message):
    with open('Key.txt') as f:
        lines = f.readlines()
    lines = str(lines)
    lines = lines.replace("'", "")
    lines = lines.replace("[", "")
    lines = lines.replace("]", "")
    lines = lines.replace(")", "")
    lines = lines.replace("(", "")
    lines = lines.replace(",", "")
    lines = lines.replace(" ", "")
    key = lines
    dekey(key,keyarray)
    output = depolygraph(message)
    output = deceasarcypher(output)
    output = decryptreversal(output)
    return(output)
                
def reverse(message):
    reversedmessage = str("")
    for char in message:
        reversedmessage = str((char + reversedmessage))
    message = reversedmessage
    return message

def cCypher(message):
    global keyarray
    r = int(keyarray[0])     
    ceasarmessage = str("")
    for char in message: 
        letter = ord(char)+r
        letter = chr(letter)
        ceasarmessage = str(ceasarmessage + letter)
    message = ceasarmessage
    return message
     
def polygraph(message):
    global errors
    errors = int(0)
    global keyarray
    rounds = int(126-32)
    polymessage = str("")
    polykey = (str(""))
    polyarray = []
    polyrand = int(random.randint(32,126))
    for x in keyarray:
        if x >= 4:
            polyarray.append(x)
    for char in message:
        letter = polyarray[ord(char)-32]
        letter = chr(letter)
        if ord(letter) - 32 <= rounds: 
            polymessage = str(polymessage + letter)
        else:
            errors = errors + 1
    message = polymessage
    print(errors + " errors")
    return message

def Kumalalatest():
    rounds = int(input())
    x = int(0)
    savesta = ("")
    while x < rounds:
        savesta = savesta + (chr(x) + " " + str(x))
        x = x+1

def chartest(message):
    gooba = ("")
    for char in message:
        gooba = gooba + (int(ord(char))) + str(".")

def Encrypt(keyid, message): 
    with open(f'keys/{keyid}.txt') as f:
        lines = f.readlines()
    lines = str(key) 
    lines = lines.replace("'", "")
    lines = lines.replace("[", "")
    lines = lines.replace("]", "")
    lines = lines.replace(")", "")
    lines = lines.replace("(", "")
    lines = lines.replace(",", "")
    lines = lines.replace(" ", "")
    #print(lines)
    key = lines
    dekey(key,keyarray)
    output = reverse(message)
    output = cCypher(output)
    return polygraph(output) 
    
if __name__ == "__main__":
    GenerateKey()