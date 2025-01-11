#V2: Use in-function KeyArrays
#Note I wrote the encryption software I used for this program as one of my first real projects. It is outdated in compariston to my actual skills, but may have some remnants in theis altered version of it.
import random
keyarray = [0,0,0,0]

def GenerateKey(*args):
    global keyarray
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
            if polyrand != 124:
                polyarray.append(polyrand)
                polykey = str(polykey + "|"+ str(polyrand))
                x = x+1
            polyrand = int(random.randint(32,99))
        if polyarray.count(polyrand) != 0:
            if int(len(polyarray)) < int(99-32):
                polyrand = int(random.randint(32,99))
            else:
                polyrand = int(random.randint(32,126))
    keyarray.append(str(polykey))
    key = ""
    key = "".join(map(str, keyarray))
    try:
        open("Key.txt", "r").close
    except:
        with open("Key.txt", "w") as keyfile:
            keyfile.write(key)
            keyfile.close()
    return open("Key.txt", "r").read()

def dekey(text):
    global keyarray
    array = [0,0,0,0]
    xvar = int(0)
    while xvar < 3:
        for char in text: 
            array[xvar] = int(char)
            xvar = int(xvar) + 1
            if xvar == 4:
                break
    larray = text.split("|")
    for x in larray:
        if int(larray.index(x)) >= 1:
            array.append(int(x))
    print(array)
    keyarray = array
    
def decryptreversal(message ,*args):
   versedmessage = str("")
   for char in message:
        versedmessage = str(char + versedmessage)
   return versedmessage

def deceasarcypher(message ,*args):
    r = int(keyarray[0])
    ceasarmessage = str("")
    for char in message:
        letter = ord(char)-r
        letter = chr(letter)
        ceasarmessage = str(ceasarmessage + letter)
    return(ceasarmessage ,*args)

def depolygraph(message ,*args):
    global keyarray
    polymessage = str("")
    for char in str(message ,*args):
        letter = int(ord(char))
        letter = keyarray.index(letter)
        letter = chr(letter+32-4)
        polymessage = str(polymessage + letter)
    return(polymessage ,*args)

def Decrypt(message,*args):
    global keyarray
    with open('Key.txt') as f:
        lines = f.readlines()
        f.close
    key = lines
    dekey(key)
    output = depolygraph(message)
    output = deceasarcypher(output)
    output = decryptreversal(output)
    return(output)
                
def reverse(message ,*args):
    reversedmessage = str("")
    for char in message:
        reversedmessage = str((char + reversedmessage))
    message = reversedmessage
    return message

def cCypher(message ,*args):
    global keyarray
    r = int(keyarray[0])     
    ceasarmessage = str("")
    for char in message: 
        letter = ord(char)+r
        letter = chr(letter)
        ceasarmessage = str(ceasarmessage + letter)
    message = ceasarmessage
    return message
     
def polygraph(message ,*args):
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
    print(f'{errors} errors')
    return message

def Kumalalatest():
    rounds = int(input())
    x = int(0)
    savesta = ("")
    while x < rounds:
        savesta = savesta + (chr(x) + " " + str(x))
        x = x+1

def chartest(message ,*args):
    gooba = ("")
    for char in message:
        gooba = gooba + (int(ord(char))) + str(".")

def Encrypt(keyid, message ,*args): 
    global keyarray
    with open(f'Data/keys/{keyid}.txt') as f:
        lines = f.read()
    #print(lines)
    key = lines
    dekey(key)
    print(message)
    output = reverse(message)
    print(f'reversed: {output}')
    output = cCypher(output)
    print(f'roated: {output}')
    output = polygraph(output)
    print(f'polygraphed: {output}')
    return output
    
if __name__ == "__main__":
    GenerateKey()