while True:
    nilai = int (input("input (1-7) : "))
    hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

    if nilai < 1 or nilai > 7:
        print("Nilai Tidak valid")
        continue
    else:
        print(f"Hari ini adalah {hari[nilai-1]}")
