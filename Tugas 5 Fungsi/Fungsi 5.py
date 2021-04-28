import time
def Penjumlahan( *vartuple):
    print('Jumlahnya adalah:')
    jumlah=0
    for var in vartuple:
        jumlah = jumlah + var
    print(jumlah)

def rerata( *vartuple):
    print('Rata-ratanya adalah')
    rata = 0
    total = 0
    for var in vartuple:
        total = total + var
    rata = total / len(vartuple)
    print(rata)

print('Alright, basic math')
time.sleep(0.5)
print('Masukkan 4 angka yang akan dijumlahkan ')
A = input('Angka 1 ')
B = input('Angka 2 ')
C = input('Angka 3 ')
D = input('Angka 4 ')
time.sleep(0.7)
print('Ok, that simple, next')
time.sleep(0.5)
print('Masukkan 4 angka yang ingin dicari rata-ratanya')
E = input('Angka 1 ')
F = input('Angka 2 ')
G = input('Angka 3 ')
H = input('Angka 4 ')
time.sleep(1.0)
print('Hmmm susah ini, mohon tunggu sebentar')
time.sleep(1.0)
print('.')
time.sleep(1.0)
print('.')
time.sleep(1.0)
print('.')
time.sleep(2.5)
print('Ah susah, ganti-ganti') #Kodingnya susah, nggak bisa masukkin input ke vartuplenya ):
time.sleep(1.0)
print('Penjumlahan : 32, 54, 32, 65')
print('rerata : 543, 46, 321, -90')
time.sleep(1.3)
print('Nah ini baru gampang, tunggu')
time.sleep(1.0)
print('Processing...')
time.sleep(2.0)
Penjumlahan(32, 54, 32, 65)
rerata(543, 46, 321, -90)