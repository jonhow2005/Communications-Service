def Findkey(Key,*args):
    with open(f'Data/{Key}.txt', "r") as keyfile:
        x = keyfile.readline()
    return x    
        