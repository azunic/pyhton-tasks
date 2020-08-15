#Napišite program u kojem korisnik unos
#i N dvoznamenkastih brojeva. Korisnik unosi N. Prog
#ram treba ispisati najveći i najmanji broj. 
#Koristite funkciju „MaksIMin” koja prima vrijednost N i ne
# vraća rezultat. Funkcija mora 
#ispisati najveći i najmanji broj koje je korisnik unio. 
#Koristite funkcije „Maks” i „Mini” koje primaju dva bro
#
#ja i vraćaju veći (maks), odnosno manji (mini), od njih dva.

#PROVJERIT //

def Maksimalni(N):
    lista = []

    for i in range(0, N):
        broj = int(input("Unesite broj: "))
        lista.append(broj)
    
    max_broj = lista[0]
    min_broj = lista[0]
    for broj in lista:
        
        if(broj < min_broj):
            min_broj = broj 
            
        if(broj > max_broj):
            max_broj = broj
            
    print("Minimalni broj: ", min_broj)
    print("Maksimalni broj: ", max_broj)
    

N = int(input("Unesite broj"))
Maksimalni(N)


   