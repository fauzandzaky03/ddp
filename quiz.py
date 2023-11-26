nama_kendaraan = input ('masukan nama kendaraan?')
jenis_bensin = input ('masukan jenis bensin?')
kota = input ('masukan kota?')

if jenis_bensin == 'pertalite':
    harga = 10000
    jarak_tempuh = 12

elif jenis_bensin == 'pertamax':
    harga = 14000
    jarak_tempuh = 13
elif jenis_bensin == 'pertamaxturbo':
    harga = 17000
    jarak_tempuh = 13.5
else :
    print("")

if kota == 'jakarta':
    jarak_kota = 20

elif kota == 'bekasi':
    jarak_kota = 35.7

elif kota == 'depok':
    jarak_kota = 5

elif kota == 'tanggerang':
    jarak_kota = 99

elif kota == 'bogor':
    jarak_kota = 120.6
else :
    print("")

pemakaian_bensin = (jarak_tempuh / jarak_kota)
harga_bensin = int(pemakaian_bensin * harga)

print(nama_kendaraan, 'nama kendaraan')
print(jenis_bensin, 'jenis bensin')
print(kota, 'kota')
print('pemakaian bensin', pemakaian_bensin, )
print(harga, 'harga')

#tugas3 



