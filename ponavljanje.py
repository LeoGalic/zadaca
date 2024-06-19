import random


imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']


radnici = []
for _ in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = round(random.uniform(4, 6), 2)
    radnici.append({"ime": ime, "prezime": prezime, "satnica": satnica})


for radnik in radnici:
    radnik["tjedni_sati"] = random.randint(20, 30)


isplate = []
for radnik in radnici:
    isplata = radnik["satnica"] * radnik["tjedni_sati"]
    isplate.append((radnik["ime"], radnik["prezime"], isplata))


for isplata in isplate:
    print(isplata)


ukupna_isplata = sum(isplata[2] for isplata in isplate)
prosječna_isplata = ukupna_isplata / len(isplate)

print("\nUkupna isplata:", ukupna_isplata)
print("Prosječna isplata:", round(prosječna_isplata, 2))


print("\nRadnici sa isplatom iznad prosječne:")
for isplata in isplate:
    if isplata[2] > prosječna_isplata:
        print(isplata[0], isplata[1])