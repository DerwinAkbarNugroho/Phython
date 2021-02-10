Angka = int(input('Masukkan Angka: '))

faktorial = 1

if Angka<0:
    print('Gak bisa negatif, sudah begitu aturannya sejak ribuan tahun yang lalu')
elif Angka == 0:
    print('Faktorial dari', Angka, 'adalah 1')
else:
    for i in range(1, Angka+1):
        faktorial= faktorial*i
    print('Faktorial dari', Angka, 'adalah', faktorial)
