user_input="q"
meglevobejegyzesek = []
print("Üdvözlöm!")
import hashlib
import os
biztonsagikerdesek=["Kérem írja be mi a kedvenc szine: ","Kérem írja be a házi állata nevét: ", "Kérem írja be szerelme nevét: ", "Kérem írja be az általános iskolájának nevét: ", "Kérem írja be a kedvenc étele nevét: "]
while user_input!="":
    user_input=input("Kérem írja be mit szeretne csinálni: ")
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
        if jelszo!=megerosito:
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

        with open('regisztralt.txt', 'a', encoding='utf-8') as celfajl:
            print(f'{felhasznaloneve}+{password}+{kerdesek_sorszama}+{bizt_valaszok}+', file=celfajl) 

    
    def bejelentkezes():
        
        with open('regisztralt.txt', 'r') as file:
            for sor in file:
                adat=sor.split("+")
                jelszoprobalas = 3 
                while jelszoprobalas != 0:
                    username=input("Add meg a felhasználó neved: ")
                    pw=input("Add meg a jelszót: ")
                    titok = hashlib.sha256(pw.encode())
                    password = titok.hexdigest()
                    if adat[0]!=username or adat[1]!=password: 
                        jelszoprobalas -=1
                        print(f"Hibás felhasználónév vagy jelszó. Hátralévő próbálkozások: {jelszoprobalas}")
                    elif adat[0]==username and adat[1]==password:
                        print("A felhasználónév és a jelszó is egyezik!")
                        break
                    if jelszoprobalas == 0:
                        break
                if jelszoprobalas == 0:
                    print("Nem jól adtad meg a felhasználó nevet vagy a jelszót\nA biztonsági kérdések következnek: ")

                    
                    cleaned = adat[2].replace("[", "").replace("]", "")
                        
                    vegso = list(map(int, cleaned.split(", ")))
                    cleaned_bizt = adat[3].replace("[", "").replace("]", "").replace("'","")
                    vegso_bizt=list(cleaned_bizt.split(", "))

                    belepve=True
                    for a in vegso:
                        bizt_kerdes=input(f"{biztonsagikerdesek[a]}")
                        titok = hashlib.sha256(bizt_kerdes.encode())
                        titkositva_biz_kerd = titok.hexdigest()
                        if vegso_bizt[a]==titkositva_biz_kerd:
                            print("Helyes válasz!")
                            
                        else:
                            belepve=False
                        
                    if belepve:
                        print("Sikersen beléptél!") 

    
    
    def UjBejegyzes():
        fajlnev = 'bejegyzesek.txt'
        if os.path.exists(fajlnev):
            with open(fajlnev, 'r', encoding='utf-8') as celfajl:
                meglevobejegyzesek = [sor.strip() for sor in celfajl.readlines()]

        while True:
            bejegyzesnev = input("Kérem adja meg a bejegyzés nevét: ").strip()
            if bejegyzesnev == "":  
                megjelenites = input("Szeretné látni a meglévő bejegyzéseket? (igen/nem): ").strip().lower()
                if megjelenites == "igen":
                    print("Meglévő bejegyzések:", meglevobejegyzesek)
                kerdes = input("Szeretne új bejegyzést létrehozni? (igen/nem): ").strip().lower()
                if kerdes != "igen":
                    print("Kilépés a bejegyzés létrehozásból.")
                    break
            else:
                meglevobejegyzesek.append(bejegyzesnev)

 
        with open(fajlnev, 'w', encoding='utf-8') as celfajl:
            for bejegyzes in meglevobejegyzesek:
                celfajl.write(bejegyzes + '\n')
        
    def Modositas():
        fajlnev = 'bejegyzesek.txt'
        if os.path.exists(fajlnev):
            with open(fajlnev, 'r', encoding='utf-8') as celfajl:
                meglevobejegyzesek = [sor.strip() for sor in celfajl.readlines()]
        
        
        modositas = "a"
        while modositas != "":
            print(meglevobejegyzesek)
            modositas = input("Melyiket szeretné módosítani? Adja meg a sorszámát: ")
            if modositas != "":
                sorszam = int(modositas)
            if not(0<sorszam <= len(meglevobejegyzesek)):
                print("Nem megfelelő a sorszám!")
                modositas = int(input("Melyiket szeretné módosítani? Adja meg a sorszámát: "))
            if 0<sorszam <= len(meglevobejegyzesek) and modositas != "":
                biztos = input(f"Biztos, hogy szeretné módosítani ezt: {meglevobejegyzesek[sorszam-1]}? (igen/nem): ").strip().lower()
                if biztos == "igen":
                    del meglevobejegyzesek[sorszam-1]
                    modositott = input("Adja meg a módosított bejegyzés nevét: ")
                    meglevobejegyzesek.append(modositott)
                    print("Sikeresen módosítva!")
                else:
                    print(meglevobejegyzesek)
                    modositas = int(input("Melyiket szeretné módosítani? Adja meg a sorszámát: "))
                    if modositas != "":
                        sorszam = int(modositas)

        with open(fajlnev, 'w', encoding='utf-8') as celfajl:
                    for bejegyzes in meglevobejegyzesek:
                        celfajl.write(bejegyzes + '\n')

     
    if user_input=="regisztrálni":
        regisztralni()
    if user_input=="bejelentkezni":
        bejelentkezes()
    if user_input=="új bejegyzést létre hozni":
        UjBejegyzes()
    if user_input=="módosítani":
        Modositas()  
    
