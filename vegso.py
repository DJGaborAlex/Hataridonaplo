import os
import json
import hashlib
from datetime import datetime

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

def validate_date(input_date):
    try:
        date_obj = datetime.strptime(input_date, "%Y-%m-%d")
        if date_obj < datetime.now():
            print("A határidő nem lehet a múltban.")
            return None
        return date_obj
    except ValueError:
        print("Nem megfelelő formátum, kérem használja a (YYYY-MM-HH) formátumot.")
        return None

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
    
def login():
    data = load_data()
    username = input("Add meg a felhasználó neved: ")
    if username not in data:
        print("Nem létezik a felhasználónév.")
        return None
    passwordtry = 3
    while passwordtry !=0:
        password = input("Add meg a jelszót: ")
        user = data[username]
        if hash_password(password, user["salt"]) == user["password"]:
            print("Sikeres belépés!")
            return username
        else:
            print(f"Helytelen jelszó! ({passwordtry-1} próbálkozásod maradt)")
            passwordtry -= 1
    answer = input(user["security_question"] + " ")
    if hash_password(answer, user["salt"]) == user["security_answer"]:
        print("A biztonsági kérdések helyesen megválaszolva, sikeres belépés!")
        return username
    print("Sikertelen belépés!")
    return None

def add_task(username):
    data = load_data()
    task = input("Adja meg a feladat leírását: ")
    while True:
        deadline = input("Adja meg a határidőt (YYYY-MM-DD): ")
        valid_date = validate_date(deadline)
        if valid_date:
            break
    data[username]["tasks"].append({"task": task, "deadline": deadline, "status": "Folyamatban"})
    save_data(data)
    print("Feladat sikeresen hozzáadva!")

def view_tasks(username):
    data = load_data()
    tasks = data[username]["tasks"]
    if not tasks:
        print("Nincs feladat.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {task['deadline']} - {task['status']}")
    print()

def mark_task_complete(username):
    data = load_data()
    view_tasks(username)
    try:
        task_number = int(input("Adja meg készre állítandó feladat sorszámát: "))
        if 0 < task_number <= len(data[username]["tasks"]):
            data[username]["tasks"][task_number - 1]["status"] = "Kész"
            save_data(data)
            print("Feladat készre állítva.")
        else:
            print("Nem megfelelő sorszám.")
    except ValueError:
        print("Adjon meg egy helyes sorszámot.")
        
def delete_task(username):
    data = load_data()
    view_tasks(username)
    try:
        task_number = int(input("Adja meg a törölni kívánt feladat sorszámát: "))
        if 0 < task_number <= len(data[username]["tasks"]):
            del data[username]["tasks"][task_number - 1]
            save_data(data)
            print("Feladat törölve.")
        else:
            print("Nem megfelelő sorszám.")
    except ValueError:
        print("Adjon meg egy helyes sorszámot.")
        
def main():
    while True:
        print("1. Regisztrálás")
        choice = input("Mit szeretne csinálni: ")
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                while True:
                    print("1. Feladat létrehozása\n2. Feladatok megtekintése\n3. Feladat készre állítása\n4. Feladat törlése\n5. Kijelentkezés")
                    user_choice = input("Mit szeretne csinálni: ")
                    if user_choice == "1":
                        add_task(username)
                    elif user_choice == "2":
                        view_tasks(username)
                    elif user_choice == "3":
                        mark_task_complete(username)
                    elif user_choice == "4":
                        delete_task(username)
                    elif user_choice == "5":
                        print("Kijelentkezve.")
                        break
                    else:
                        print("Érvénytelen opció.")
        elif choice == "3":
            print("Viszlát!")
            break
        else:
            print("Érvénytelen opció.")

if __name__ == "__main__":
    main() 
