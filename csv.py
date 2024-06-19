import csv


def ucitaj_podatke(putanja_do_datoteke):
    studenti = []
    with open(putanja_do_datoteke, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            ime = row[0]
            prezime = row[1]
            bodovi = int(row[2])
            studenti.append((ime, prezime, bodovi))
    return studenti


def ispisi_polozene(studenti):
    for student in studenti:
        if student[2] > 49:
            print(student)


def sortiraj_po_prezimenima(studenti):
    return sorted(studenti, key=lambda student: student[1])

def kreiraj_rezultate_po_ocjenama(studenti):
    ocene = {
        "Nedovoljan": 0,
        "Dovoljan": 0,
        "Dobar": 0,
        "Vrlodobar": 0,
        "Izvrstan": 0
    }
    
    for student in studenti:
        bodovi = student[2]
        if bodovi < 50:
            ocene["Nedovoljan"] += 1
        elif 50 <= bodovi <= 65:
            ocene["Dovoljan"] += 1
        elif 66 <= bodovi <= 80:
            ocene["Dobar"] += 1
        elif 81 <= bodovi <= 90:
            ocene["Vrlodobar"] += 1
        elif 91 <= bodovi <= 100:
            ocene["Izvrstan"] += 1
            
    return ocene


putanja_do_datoteke = 'rezultati.csv'


studenti = ucitaj_podatke(putanja_do_datoteke)


print("Studenti koji su položili ispit:")
ispisi_polozene(studenti)


studenti_sortirani = sortiraj_po_prezimenima(studenti)
print("\nStudenti sortirani po prezimenima:")
for student in studenti_sortirani:
    print(student)


ocene = kreiraj_rezultate_po_ocjenama(studenti)
print("\nBroj ostvarenih ocjena po bodovnom rangu:")
for ocena, broj in ocene.items():
    print(f"{ocena}: {broj}")