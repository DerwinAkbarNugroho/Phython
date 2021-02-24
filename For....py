sum= int(input('Masukkan angka awalnya '))
angka= int(input('masukkan pertambahan angka di setiap looping (harus positif): '))
batas= int(input('Masukkan batas looping (positif): '))
for each in range(1,batas):
    print(sum, 'adalah angka pertamanya')
    print('Sekarang angka itu menjadi')
    sum = sum + angka
    if (sum % 2 == 0 ):
        print (sum, 'yang merupakan angka genap')
    else:
       print (sum, 'yang merupakan angka ganjil')
print('Looping telah sukses dan selesai!!!1!1!1!1')