word = str(input('Masukkan kalimat yang ingin diuji: '))
huruf_1 = str(input('masukkan huruf yang ingin diketahui jumlahnya: ')) # Jika dirasa cukup, kosongkan saja. Jika ingin mencari huruf lagi, ditambah saja dibawah huruf_5, huruf_6, dst
huruf_2 = str(input('masukkan huruf yang ingin diketahui jumlahnya: '))
huruf_3 = str(input('masukkan huruf yang ingin diketahui jumlahnya: '))
huruf_4 = str(input('masukkan huruf yang ingin diketahui jumlahnya: '))

jum_1 = 0
jum_2 = 0
jum_3 = 0
jum_4 = 0

for letter in word:
    if letter == huruf_1:
        jum_1 += 1
        continue
print('huruf', huruf_1,'berjumlah : ', jum_1)
for letter in word:
    if letter == huruf_2:
        jum_2 += 1
        continue
print('huruf', huruf_2, 'jumlah : ', jum_2)
for letter in word:
    if letter == huruf_2:
        jum_3 += 1
        continue
print('huruf', huruf_3, 'jumlah : ', jum_3)
for letter in word:
    if letter == huruf_4:
        jum_4 += 1
        continue
print('huruf', huruf_4, 'jumlah : ', jum_4)