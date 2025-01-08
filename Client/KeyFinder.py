def Findkey(Key,*args):
    with open(f'{Key}.txt', "r") as keyfile:
        x = keyfile.readline()
    return x    
        