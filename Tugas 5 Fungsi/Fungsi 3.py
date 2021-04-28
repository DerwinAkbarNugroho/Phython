import time
def FPB(X, Y):
    if X>Y:
        kecil = Y
    else:
        kecil = X
    for i in range(1, kecil+1):
        if ((X % i == 0) and (Y % i == 0)):
            fpb = i
    return fpb
print('aight, lets start...')
time.sleep(0.7)
num_1 = int(input('Angka pertama... '))
num_2 = int(input('Angka kedua... '))
time.sleep(0.5)
print('Processing...')
time.sleep(1.5)
print('FPB dari', num_1, 'dan', num_2, 'adalah', FPB(num_1, num_2))