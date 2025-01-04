import os
import json
import hashlib

data_file = "data.json"

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def load_data():
    if not os.path.exists(data_file):
        return {}
    with open(data_file, "r") as file:
        return json.load(file)

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)
def register():
    data = load_data()
    username = input("Adja meg a felhasználónevét: ")
    if username in data:
        print("Ez a felhasználónév már létezik.")
        return
    password = input("Adja meg a jelszavát: ")
    security_question = input("Adjon meg egy biztonsági kérdést: ")
    security_answer = input("Adja meg a válaszát a kérdésnek: ")
    salt = os.urandom(16).hex()
    data[username] = {
        "password": hash_password(password, salt),
        "security_question": security_question,
        "security_answer": hash_password(security_answer, salt),
        "salt": salt,
        "tasks": []
    }
    save_data(data)
    print("Sikeres regisztrálás!")
def main():
    while True:
        print("1. Regisztrálás")
        choice = input("Mit szeretne csinálni: ")
        if choice == "1":
            register()
        elif choice == "3":
            print("Viszlát!")
            break
        else:
            print("Érvénytelen opció.")

if __name__ == "__main__":
    main() 
