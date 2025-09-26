nilai = int(input("Masukkan nilai : "))

print(f"\nTabel perkalian {nilai}:")
for i in range(1, 11):  # dari 1 sampai 10
    hasil = nilai * i
    print(f"{nilai} x {i} = {hasil}")