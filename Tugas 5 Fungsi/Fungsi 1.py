def cek_nilai(A):
    if A % 2 == 0:
        A += 2
    else:
        A *= 2
    return A
B = input('Nilainya berapa? ')
C = cek_nilai(int(B))
print('Hasilnya adalah {}'.format(C))