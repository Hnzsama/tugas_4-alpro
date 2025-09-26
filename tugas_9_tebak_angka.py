nilai = int(input("masukan nilai: "))

while True:
    guest = int(input("Masukan tebakan: "))
    print(f"Tebakan {guest} belum benar")
    if (guest > nilai):
        print("Terlalu besar")
    elif (guest < nilai):
        print("Terlalu kecil")
    elif (guest == nilai):
        break

print(f"Tebakan {guest} benar")
