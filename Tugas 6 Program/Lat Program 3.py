A= int(input('Masukkan angka pertama: '))
B= int(input('Masukkan angka kedua: '))
C= int(input('Masukkan angka ketiga: '))
D= int(input('Masukkan angka keempat: '))
E= int(input('Masukkan angka kelima: '))
F= int(input('Masukkan angka keenam: '))
x = [[A,D], 
     [B,E], 
     [C,F]]
hasil = [[0,0,0],[0,0,0]]
 
for i in range(len(x)):
    for j in range(len(x[0])):
        hasil[j][i] = x[i][j]
 
for h in hasil:
    print(h)