kecil= 0
besar= int(input('Masukkan batas angka yang akan dicari ')) 
print('bilangan prima antara',kecil,'dan',besar,'adalah')
 
for num in range(kecil, besar+1):
    if num > 1:
        for i in range(2, num):
            if (num%i)==0:
                break
        else:
            print(num)