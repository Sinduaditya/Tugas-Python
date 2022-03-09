# latihan 1

bil = input('Masukkan Sebuah Bilangan:')
bil = int(bil)
if bil % 3 == 0:
    print(bil, 'habis dibagi 3') 

# latihan 2
nama = input('Masukkan Nama Anda :')
jk = input('Anda Pria/Wanita ?')
if jk == "Pria":
        print('Hai Bro', nama)
else :
        print('Hai Sis', nama)

# lathihan 3
nama = input("Masukkan Nama Anda:")
born = input('Tahun Berapa Anda lahir ?:')
born = int(born)
if born > 1944 and born <=  1964:
    print(nama,'berdasarkan tahun lahir anda tergolong Baby Boomer')
elif born > 1965 and born <= 1979:
    print(nama,'berdasarkan tahun lahir anda tergolong Generasi X ')
elif born > 1980 and born <= 1994:
    print(nama,'berdasarkan tahun lahir anda tergolong Generasi Y ')
elif born > 1995 and born <= 2015:
    print(nama,'berdasarkan tahun lahir anda tergolong Generasi Z ')
else :
    print('Maaf Tahun Anda Tidak Termasuk Dalam Range Daftar')