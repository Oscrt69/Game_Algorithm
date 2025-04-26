file = 'data.xlsx'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def username_exists(username):
    if not os.path.exists(file):
        return False
    with open(file, 'r') as f:
        for line in f:
            _, existing_username, _ = line.strip().split(',')
            if existing_username == username:
                return True
    return False

def save_user(username, password):
    waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hashed_password = hash_password(password)
    with open(file, 'a') as f:
        f.write(f"{waktu},{username},{hashed_password}\n")


def login(username, password):
    if not os.path.exists(file):
        return False
    hashed_password = hash_password(password)
    with open(file, 'r') as f:
        for line in f:
            _, existing_username, existing_password = line.strip().split(',')
            if existing_username == username and existing_password == hashed_password:
                return True
    return False
   
""""
def lirik():
    baris_kalimat = [
        [("Italian Brainrot", 0.1), (" Games", 0.05), (" ", 2)], 
        [("By Oscar", 0.1), (" ", 2)], 
        [("Getting Started in", 0), (" 5", 0.5), (" 4", 0.5), (" 3", 0.5), (" 2", 0.5), (" 1", 0.5)], 
    ]

    for baris in baris_kalimat:
        for kata, jeda in baris:
            for huruf in kata:
                print(huruf, end='', flush=True)
                sleep(jeda)
        print()
lirik()    
"""
sleep(1)  
clear()

print("\n========== WELCOME TO SIMPLE ALGORITHM GAME ==========")
while True:
    validate = str(input("New user? (y/n)\n"))
    if (validate == 'y'): ####
        while True:
            username = input("Enter Username : ")
            if username_exists(username):
                print("Username already exist.\n")
                continue
            password = input("New Password : ")
            save_user(username, password)
            print("Registrasi berhasil!\n")
            break
    elif (validate == 'n'): ###
         while True:
            username = input("Username: ")
            password = input("Password: ")
            if login(username, password):
                print("Login berhasil!\n")
                break
            else:
                print("Username atau Password anda salah. Coba lagi!\n")
    else:
        print("Not valid, please enter correct input")
    break

print("Choose your character: \n")
print("1. Bombardiro Crocodilo\n")
print("2. Tralalero Tralala\n")
print("3. Tung Tung Tung Sahur\n")
