nilai = int(input("Masukan nilai: "))

is_bukan_prima = True

if nilai == 0 or nilai == 1:
    is_bukan_prima = True
elif nilai == 2:
    is_bukan_prima = False
elif nilai > 2:
    for i in range(2, nilai):
        # print(i)
        if (nilai % i) == 0:
            is_bukan_prima = True
            break
        else: 
            is_bukan_prima = False

if is_bukan_prima:
    print(f"{nilai} bukanlah bilangan prima")
else:
    print(f"{nilai} adalah bilangan prima")
