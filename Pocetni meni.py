invertar = [420]
print("*"*44)
print("1. Invertar\n2. Izmeni stanje invertara\n3. Recepti\n4. Meni\n5. Izlaz")
opcija = input("Izaberite opciju: ")
opcija = int(opcija)

while(True):
    print("*"*44)
    print("1. Invertar\n2. Izmeni stanje invertara\n3. Recepti\n4. Meni\n5. Izlaz")
    opcija = input("Izaberite opciju: ")
    opcija = int(opcija)
    #Ulaskom u prvu opciju trebamo biti u mogucnosti da izlistamo invertar i izadjemo. Ideja je da mozemo i da odstampamo listu sa invertarom
    if opcija == 1:
        print(("-"*18)+"INVERTAR"+("-"*18))
        print("\n1. Pretrazi\n2. Izadji")
    #Ovde bi trebali imati opciju za dodavanje i brisanje sa liste
    if opcija == 2:
        print(("-"*15)+"IZMENI STANJE"+("-"*16))
    #Ovde bi trebalo moci dodati i ukloniti recepte
    if opcija == 3:
        print(("-"*18)+"RECEPTI"+("-"*19))
        print("1. Dodaj recept\n2. Ukloni recept\n3. Lista recepata\n4. Izadji")
    #Opcija za dodavanje, uklanjanje proizvoda i prikaz celog menija
    if opcija == 4:
        print(("-"*20)+"MENI"+("-"*20))
        print("1. Dodaj novi proizvod\n2. Ukloni proizvod\n3. Prikazi meni\n4. Izadji")
    #Izlazak iz programa
    if opcija == 5:
        break        
