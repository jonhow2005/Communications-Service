def GrabConvo(type, chat):
    with open(f'Chats/{type}/{chat}', "r") as file:
        return file.read()
    