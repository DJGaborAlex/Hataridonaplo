import hashlib
allapot="W"

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
                hatarido=input("mikorra")
                
                aktualis=[tevekenység, hatarido]
                teendo.append(aktualis)
                vege=input("szeretnél még? :")
            
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
