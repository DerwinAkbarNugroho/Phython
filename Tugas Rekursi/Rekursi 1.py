def konversi(num):
    if num > 1:
        konversi(num//2)
    print(num % 2, end=' ')

num= int(input('Masukkan angka desimal '))
konversi(num)
print()