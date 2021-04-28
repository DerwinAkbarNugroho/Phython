import time
def Faktor(X):
    print('Processing...')
    time.sleep(0.5)
    print('.')
    time.sleep(0.7)
    print('..')
    time.sleep(1)
    print('Faktor dari', X, 'adalah :')
    time.sleep(0.5)
    print('................................')
    for i in range(1, X+1):
        if X %i == 0:
            print(i)
            time.sleep(0.7)
    print('Sudah semua :)')
Angka = int(input('Masukkan Angka '))
Faktor(Angka)