def generiraj_parne(broj):
    for i in range(broj):
        if i % 2 == 0:
            yield i


def generiraj_neparne(broj):
    for i in range(broj):
        if i % 2 != 0:
            yield i

parametar = int(input("Unesite broj: "))


print("Parni brojevi:")
for parni in generiraj_parne(parametar):
    print(parni, end=" ")
print()


print("Neparni brojevi:")
for neparni in generiraj_neparne(parametar):
    print(neparni, end=" ")
print()