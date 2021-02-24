num = int(input('Masukkan sebuah angka: '))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, 'bukan bilangan prima')
            print(i,'dikali',num//i,'sama dengan',num) #i adalah angka terdekat dari 2 keatas yang bisa membagi habis angka awal
            break
    else:
        print(num,'adalah bilangan prima')
else:
    print(num,'bukan bilangan prima')
print('Aaaand thats all')