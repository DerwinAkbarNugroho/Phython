def deret(n):
    if n <= 1:
        return n
    else:
        return(deret(n-1) + deret(n-2))
    
jumlah = int(input('Mau berapa banyak? '))
 
if jumlah <= 0:
    print('ERROR 404')
else:
    print('Daftar deret: ')
    for i in range(jumlah):
        print(deret(i))