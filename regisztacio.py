allapot="W"

while allapot!="":
    def regisztracio():
        user=input()
        pw=input()
        with open('regisztralt.txt', 'a', encoding='utf-8') as celfajl:
            print(f'{user}, {pw}', file=celfajl)  
    

    allapot=input("Kérem írja be, hogy mit szeretne regisztrálni vagy bejelentkezni: ")
    if allapot =="r":
        regisztracio()
