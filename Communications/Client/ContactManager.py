
def GetContacts():
    try:
        Contacts = ""
        with open(f'Contacts.txt','r') as f:
            Contacts = f.read()
            return Contacts
    except FileNotFoundError:
        print("Contacts.txt not found. Returning empty list.")
        return Contacts
    
def GetGC():
    try:
        Contacts = ""
        with open(f'GroupChats.txt','r') as f:
            Contacts = f.read()
            return Contacts
    except FileNotFoundError:
        print("GroupChats.txt not found. Returning empty list.")
        return Contacts
    
def GetPrivs():
    try:
        Contacts = ""
        with open(f'privateChats.txt','r') as f:
            Contacts = f.read()
            return Contacts
    except FileNotFoundError:
        print("privateChats.txt not found. Returning empty list.")
        return Contacts
    
def SaveContact(ContactID, type):
    try:
        with open(f'{type}.txt','a') as f:
            f.write(ContactID + ' ')
    except Exception as e:
        print(f"Error saving contact: {e}")
        