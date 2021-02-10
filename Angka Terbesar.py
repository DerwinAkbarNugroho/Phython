bil1 = int(input('Angka Pertama '))
bil2 = int(input('Angka Kedua '))
bil3 = int(input('Angka Ketiga '))

if (bil1>=bil2) and (bil1>=bil3):
    terbesar = bil1
elif (bil2>=bil1) and (bil2>=bil3):
    terbesar = bil2
else:
    terbesar= bil3

print('Nilai terbesar adalah', terbesar)