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

N = int(input("Unesite broj"))

lista = []

for i in range(0,N):
    broj=input("Unesite broj")
    lista.append(broj)
    max_broj = lista[0]
    min_broj = lista[0]
    if(max_broj < lista[i]):
        max_broj = lista[i]
print(max_broj)
    
   