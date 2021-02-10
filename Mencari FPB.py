def hitung_FPB(X,Y):

    if X>Y:
        kecil=Y
    else:
        kecil=X
    for i in range(1, kecil+1):
        if ((X % i == 0) and (Y % i == 0)):
            FPB = i
    return FPB

Angka1 = int(input('Angka Pertama: '))
Angka2 = int(input('Angka Kedua: '))
            
print('FPB dari', Angka1, 'dan', Angka2, 'adalah', hitung_FPB(Angka1,Angka2))