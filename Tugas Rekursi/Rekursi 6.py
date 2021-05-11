import time
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i  = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print('Binary {} setara dengan {}'.format(binary1, decimal))

def binToDec(n):
    a, b = 0, 0
    for x in n[::-1]:
        if int(x) == 1:
            a += (2 ** b)
        b += 1
    return a

print('Ada 3 cara yang saya temukanuntuk mengubah binary menjadi desimal ')
time.sleep(0.6)
print('Cara pertama, dapat dari google ')
userInput = int(input('Masukkan angka binary '))
binaryToDecimal(userInput)
time.sleep(0.7)
print('Cara kedua, memakai rekursi yang menurut saya mirip dengan contoh ')
time.sleep(0.7)

X = input('tes lagi dengan angka berbeda ')
print(f'konversi dari {X} adalah {binToDec(X)}')
time.sleep(0.7)

print('Cara ketiga, sangat simpel, tapi tidak menggunakan rekursi')
c = input('Tes lagi dengan angka yang berbeda ')
d = int(c, 2)
print(c, 'bentuk desimalnya', d)