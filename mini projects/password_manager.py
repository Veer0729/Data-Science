from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("master password plz: ")
if master_pwd == "q":
    quit()
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def add():
    name = input("Account name")
    password = input("Account password")

    with open ("passwords.txt", 'a') as f:
        f.write(name + "|" + str(fer.encrypt(password.encode())) + "\n")

def view():
    with open ("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())

while True:
    mode = input("Want to add a new password or view existing ones, press q to quit? (view, add): ").lower()

    if mode == "q":
        quit()
    if mode == add:
        pass
    elif mode == view:
        pass
    else:
        print("invalid mode")
        continue