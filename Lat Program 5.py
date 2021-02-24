angka = int(input('Masukkan angka: '))
Batas = int(input('Masukkan batas perkalian + 1: ')) # Kalau misal ditulis 6, nanti perkaliannya sampai 5 saja
 
for i in range(1,Batas):
    print(angka,'X', i,'=',angka*i)