def jumlah(x):
    if x <= 1:
        return x
    else:
        return x + jumlah(x-1)

x = int(input('Masukkan angka '))   
if x < 0:
    print('ERROR 404')
else:
    print('Penjumlahan dari nilai asli', x, 'adalah', jumlah(x))