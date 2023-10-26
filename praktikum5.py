#kendaraan
kendaraan = ['Yamaha', 'Motor', '155', 'Hitam', '2roda']
print(kendaraan)

kendaraan.append('25jt')
kendaraan.append('155VVA')
kendaraan.insert(2,'Aerox')
print(kendaraan)

#hitung luas
ket = '''Selamat datang di aplikasi menghitung luas bangun datar 
masukan pilihan
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga '''

pilih = input(ket)

match pilih:
    case '1':
        print('kamu milih 1 untuk menghitung luas persegi')
        sisi = int(input('masukan sisi nya'))
        luasP = sisi*sisi
        print('luas persegi yang sisinya', sisi, 'adalah', luasP)
    case '2':
         print('kamu milih 2 untuk menghitung luas lingkaran')
         jari2 = int(input('masukan jari jari'))
         luasL = 3.14 * jari2 * jari2
         print('luas lingkaran yang jari jari nya', jari2, 'adalah', luasL)
    case '3':
         print('kamu milih 3 untuk menghitung luas segitiga')
         alas = int(input('masukan alas?'))
         tinggi = int(input('masukan tinggi?'))
         luasS = 0.5 * alas * tinggi
         print('luas segitiga yang alasnya', alas, 'dari tinggi', tinggi, 'adalah', int(luasS))
    case _:
      print('salah memilih pilihan')

         

        
