nilai = int(input("Masukkan nilai awal yang dikehendaki (positif), disarankan angka yang besar/ratusan atau ribuan: "))
batas1, batas2, batas3 = input("Masukkan 3 nilai batas yang berbeda (tulis dengan dipisah spasi dan berurutan dari kecil -> besar): ").split()
decrement1, decrement2, decrement3, decrement4 = input("Masukkan 4 angka pengurangan setiap loop (dipisah spasi), disarankan menyesuai batas dan angka awal: ").split()
while nilai > 0:
    while nilai > int(batas1):
        while nilai > int(batas2):
            while nilai > int(batas3):
                print(nilai, 'masih jauh dari 0')
                nilai -= int(decrement4)
            print(nilai, 'sudah mendekati 0')
            nilai -= int(decrement3)
        print(nilai, 'sudah jauh dari nilai awal')
        nilai -= int(decrement2)
    print(nilai, 'hampir mendekati 0')
    nilai -= int(decrement1)
print('yey sudah 0')