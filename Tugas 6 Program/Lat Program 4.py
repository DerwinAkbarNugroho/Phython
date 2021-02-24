kecil = int(input('Masukkan batas terkecilnya: '))
besar = int(input('Masukkan batas maksimalnya: '))
 
for X in range(kecil, besar + 1):
    Y = len(str(X))
    Z = 0
    AA = X
    while AA > 0:
        AB = AA % 10
        Z += AB ** Y
        AA // = 10
    
    if X == Z:
        print(X)