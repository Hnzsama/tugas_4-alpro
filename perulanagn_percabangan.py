nilai = int(input("Masukan nilai: "))
bilanganGanjil = []

for i in range(nilai):
    if ((i+1) % 2 != 0):
        bilanganGanjil.append(i+1)

jumlah = sum(bilanganGanjil)
print(f"Jumlah Bilangan ganjil {jumlah}")