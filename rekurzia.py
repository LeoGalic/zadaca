def euklidov_algoritam(a, b):
   
    if b == 0:
        return a
    
    else:
        return euklidov_algoritam(b, a % b)


a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))

nzd = euklidov_algoritam(a, b)
print(f"Najveći zajednički delilac brojeva {a} i {b} je {nzd}.")