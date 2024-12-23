def Findkey(Key):
    with open(f'{Key}.txt', "r") as keyfile:
        x = keyfile.readline()
    return x    
        