while True:
    nilai = int(input("input (1-100) : "))

    if (nilai < 1 or nilai > 100):
        print("Bilangan Tidak valid")
        continue
    else:
        if nilai > 85 and nilai <= 100:
            print(f"Predikat A, nilai {nilai}")
        elif nilai > 70 and nilai < 85:
            print(f"Predikat B, nilai {nilai}")
        elif nilai > 55 and nilai < 70:
            print(f"Predikat C, nilai {nilai}")
        elif nilai > 40 and nilai < 55:
            print(f"Predikat D, nilai {nilai}")
        else:
            print(f"Predikat E, nilai {nilai}")
        break
