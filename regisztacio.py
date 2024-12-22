allapot="W"
import hashlib
from datetime import date

mai_datum = date.today()
print("A mai dátum:", mai_datum)

while allapot!="":
    bejelentkezve=False
    def regisztracio():
        user=input()
        pw=input()
        terve=input("Szeretne most hozzá adni vagy majd később? igen vagy nem: ")
        if terve=="igen":
            vege="W"
            teendo=[]
            while vege!="nem":
                tevekenység=input("írd be mit szeretnél:")
                try:
                    hatarido=input("mikorra").split("-")
                    felh_datum=date(int(hatarido[0]), int(hatarido[1]), int(hatarido[2]))
                
                
                    if mai_datum>felh_datum:
                        print("A mai dátum nem lehet kisebb!")
                        hatarido=input("mikorra").split("-")
                    aktualis=[tevekenység, hatarido]
                    teendo.append(aktualis)
                    vege=input("szeretnél még? :")
                except ValueError:
                    print("Hiba: Nem dátumot adtál meg.")
            
        elif terve=="nem":
            tevekenység=[]
            hatarido=[]
        titok = hashlib.sha256(pw.encode())
        hexa = titok.hexdigest()
        with open('regisztralt.txt', 'a', encoding='utf-8') as celfajl:
            print(f'{user}, {hexa}, {teendo}, ', file=celfajl)  
    allapot=input("Kérem írja be, hogy mit szeretne regisztrálni vagy bejelentkezni: ")
    if allapot =="r":
        regisztracio()
