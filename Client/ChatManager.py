def GrabConvo(type, chat):
    try:
        with open(f'Data/Chats/{type}/{chat}', "r") as file:
            return file.read()
    except:
        return "-"
 
#V2 Update: Condense 

def UpdateConvo(chat, data):
    with open(f'Data/Chats/Conv/{chat}', 'a') as file:
            file.write(f'\n{data}\n')
            file.close()
            
def UpdateChat(data):
    chat,data = data.split(" ", 2)
    with open(f'Data/Chats/GC/{chat}', 'w') as file:
            file.write(f'\n{data}\n')
            file.close()
            