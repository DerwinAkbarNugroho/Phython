def faktor(x):
    if x == 1:
        return x
    else:
        return x*faktor(x-1)
print('Faktorial itu n!, jadi sebaiknya angkanya kecil saja')
x = int(input('Angkanya '))
if x < 0:
    print('Angka harus positif')
elif x == 0:
    print('Faktorial', x, 'adalah 1')
else:
    print('Faktorial', x, 'adalah', faktor(x))