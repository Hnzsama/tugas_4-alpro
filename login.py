username = "Bowok"
password = "jembut21"

attemp = 0

while attemp < 3:
    inputUsername = input("Masukan Username: ")
    inputPassword = input("Masukan Password: ")

    if inputUsername != username:
        print("Username tidak ditemukan")
        attemp += 1
        continue
    elif inputPassword != password:
        print("Password salah coy")
        attemp += 1
        continue
    elif inputUsername != username and inputPassword != password:
        print("Periksa inputan")
        attemp += 1
        continue
    elif inputUsername == username and inputPassword == password:
        print("Selamat sudah login, gak ada apa-apa sih")
        break
    
