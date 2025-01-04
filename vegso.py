fut_main=True
belepve=False
username=""
import hashlib
from datetime import date

try:
    open('b.txt', 'x').close()
    
except FileExistsError:
    pass

mai_datum = date.today()
print("A mai dátum:", mai_datum)


biztonsagikerdesek=["Kérem írja be mi a kedvenc szine: ","Kérem írja be a házi állata nevét: ", "Kérem írja be szerelme nevét: ", "Kérem írja be az általános iskolájának nevét: ", "Kérem írja be a kedvenc étele nevét: "]

def regisztralni():
        plusz=True
        while plusz:
            felhasznaloneve=input("Kérem írja be a felhasználó nevét: ")
            if "+" in felhasznaloneve:
                print("Nem lehet + a felhasznalonevébe!")
            else:
                plusz=False
        jelszo=input("Kérem írja be a jelszavát: ")
        megerosito=input("Ismételje meg a jelszavát!: ")
        while jelszo!=megerosito:
            print("A két jelszó nem egyezik!")
            jelszo=input("Kérem írja be a jelszavát: ")
            megerosito=input("Ismételje meg a jelszavát: ")
        print("Kérem írja be hány kérédést szeretne (minimum 2) (maximum 5): ")
        
        for q in range(5):
            print("------------------------------------------------------I")
            print("{}. {:^50} I".format(f"{q+1}",f"{biztonsagikerdesek[q]}"))
        print("------------------------------------------------------I")
        qw=True
        while qw:
            try:
                keredesek_szama=int(input("Kérem írja be a kérdések számát: "))
                if keredesek_szama<6 and keredesek_szama>1:
                    qw=False
                else:
                    print("2 és 5 között!")
            except ValueError:
                print("Számot adj meg!")
        szamok=True
        kerdesek_sorszama=[]
        while szamok:
            try:
                if keredesek_szama==5:
                    for i in range(5):
                        kerdesek_sorszama.append(i)
                    szamok=False
                else:
                    q=0
                    while q!=keredesek_szama:
                        kerdes=int(input("Kérem add meg a szám sorszámát:"))
                        if kerdes not in kerdesek_sorszama:
                            
                            if kerdes>0 and kerdes<6:
                                kerdesek_sorszama.append(kerdes-1)
                                q+=1
                            else:
                                print("Nincs ilyen sorszámú kérdés")
                        else:
                            print("Ezt már egyszer megadtad!")
                            
                    szamok=False
                

            except ValueError:
                print("Számokat adj meg!")


        bizt_valaszok=[]

        for t in kerdesek_sorszama:
            bkerdes=input(f"{biztonsagikerdesek[t]}")
            titok = hashlib.sha256(bkerdes.encode())
            bkerdestitkositva = titok.hexdigest()
            bizt_valaszok.append(bkerdestitkositva)

       
        titok = hashlib.sha256(jelszo.encode())
        password = titok.hexdigest()

        with open('r.txt', 'a', encoding='utf-8') as celfajl:
            print(f'{felhasznaloneve}+{password}+{kerdesek_sorszama}+{bizt_valaszok}+', file=celfajl) 


while fut_main:
    print("1. regisztrálni")
    
    print("q befejezni a kódot.")
    user_input=input("mit szeretne csinálni! ")
    if user_input=='1':
        regisztralni()
    

    elif user_input=="q":
        fut_main=False
