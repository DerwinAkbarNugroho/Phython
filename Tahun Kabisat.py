Tahun = int(input('Tahun Yang Dicari '))

if (Tahun % 4) == 0:
    if (Tahun%100) == 0:
        if (Tahun%400) == 0:
            print('{0} adalah tahun kabisat'. format(Tahun))
        else:
            print('{0} bukan tahun kabisat'. format(Tahun))
    else:
        print('{0} adalah tahun kabisat'. format(Tahun))
else:
    print('{0} bukan tahun kabisat'. format(Tahun))