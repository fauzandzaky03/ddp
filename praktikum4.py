#true
a = 'saya' 
jajan = 25000

if (jajan <= 25000):
    keterangan = 'jajan cukup'
else:
    keterangan = 'jajan berlebih'
print(a, 'jajan hari ini sebesar', jajan, keterangan)

#false

a = 'saya' 
nilai = 70

if (nilai > 80):
    keterangan = 'tidak remedial'
else:
    keterangan = 'remedial'
print(a, 'nilai pts minggu lalu', nilai, keterangan)

#elif

pembeli = 'fauzan'
nominal = 200000

if (nominal == 100000):
   ket = 'jajan di mixue'
elif (nominal >= 50000):
   ket = 'jajan di warkop'

else:
   ket = 'kamu nggak punya duit'

print('pembeli', pembeli, 'nominal belanja anda Rp.',nominal,ket)

#praktikum4

nama = 'fauzan'
prodi = 'Sistem Informasi'
nim = '0110123014'
matkul = 'DDP'
nilai = 80

if (nilai >= 90):
    ket = 'A'
elif (nilai >= 80):
    ket = 'B'
elif (nilai >= 70):
    ket = 'C'
else:
    ket = 'D'

print('nama', nama, 'prodi',prodi, 'nim', nim, 'matkul', matkul, 'nilai', nilai,ket)