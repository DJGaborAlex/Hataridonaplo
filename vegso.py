import os
import json
import hashlib
from datetime import datetime, timedelta

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
        print("Nem megfelelő formátum, kérem használja a (YYYY-MM-DD) formátumot.")
        return None

# Aktuális hét feladatai

def get_current_week_dates():

    today = datetime.today()
    
    # Hétfő dátuma (aktualizálás a heti ciklusra)
    start_of_week = today - timedelta(days=today.weekday())
    
    # Vasárnap dátuma (hét utolsó napja)
    end_of_week = start_of_week + timedelta(days=6)
    
    return start_of_week, end_of_week

def view_week_tasks(username):
    data = load_data()
    tasks = data[username]["tasks"]
    
    start_of_week, end_of_week = get_current_week_dates()

    current_week_tasks = []
    for task in tasks:
        task_deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        if start_of_week <= task_deadline <= end_of_week:
            current_week_tasks.append(task)
    
    if current_week_tasks:
        print()
        for i, task in enumerate(current_week_tasks, start=1):
            print(f"{i}. {task['task']} - {task['deadline']} - {task['status']}")
        print()
    else:
        print("Nincs feladat az aktuális hétre.")

def register():
    data = load_data()
    username = input("Adja meg a felhasználónevét: ")
    if username in data:
        print("Ez a felhasználónév már létezik.")
        return
    password = input("Adja meg a jelszavát: ")
    password2 = input("Erősítse meg a jelszavát: ")
    
    if password != password2:
        print("A két jelszó nem egyezik meg. Kérem próbálja újra.")
        return

    security_question = input("Adjon meg egy biztonsági kérdést: ")
    security_answer = input("Adja meg a válaszát a kérdésnek: ")
    os.system('cls')
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
            os.system('cls')
            return username
        else:
            print(f"Helytelen jelszó! ({passwordtry-1} próbálkozásod maradt)")
            passwordtry -= 1
    answer = input(user["security_question"] + " ")
    if hash_password(answer, user["salt"]) == user["security_answer"]:
        print("A biztonsági kérdések helyesen megválaszolva, sikeres belépés!")
        os.system('cls')
        return username
    print("Sikertelen belépés!")
    return None

def add_task(username):
    data = load_data()
    os.system('cls')
    task = input("Adja meg a feladat leírását: ")
    while True:
        deadline = input("Adja meg a határidőt (YYYY-MM-DD): ")
        os.system('cls')
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
        print()
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
    os.system('cls')
    while True:
        print("1. Regisztrálás\n2. Bejelentkezés\n3. Kilépés")
        choice = input("Mit szeretne csinálni: ")
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                while True:
                    print("1. Feladat létrehozása\n2. Feladatok megtekintése\n3. Aktuális hét feladatai\n4. Feladat készre állítása\n5. Feladat törlése\n6. Kijelentkezés")
                    user_choice = input("Mit szeretne csinálni: ")
                    if user_choice == "1":
                        add_task(username)
                    elif user_choice == "2":
                        view_tasks(username)
                    elif user_choice == "3":
                        view_week_tasks(username)
                    elif user_choice == "4":
                        mark_task_complete(username)
                    elif user_choice == "5":
                        delete_task(username)
                    elif user_choice == "6":
                        os.system('cls')
                        print("Kijelentkezve.")
                        break
                    else:
                        print("Érvénytelen opció.")
        elif choice == "3":
            os.system('cls')
            print("Viszlát!")
            break
        else:
            print("Érvénytelen opció.")

if __name__ == "__main__":
    main()
