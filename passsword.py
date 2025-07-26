from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key",'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter your master password ")

key = load_key()

fer = Fernet(key)



def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user ,pas = data.split("|")
            print("name is : ",user ,"| pass is ",fer.decrypt(pas.encode()).decode())

def add():
    name = input("enter name of the person ")
    pwd = input("enter password ")

    with open("password.txt",'a') as f:
        f.write(name+ "|"+ fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("type 'view' to view or 'add' to add and 'q' to quit ").lower()

    if mode == 'view':
        view()
        break
    elif mode == 'add':
        add()
        break
    elif mode =='q':
        break
    else:
        input("invalid")