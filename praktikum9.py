hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def predikatLulus(data):
# menggunakan list untuk mengambil nama dari hasil_akhir
# yang memiliki nilai lebih dari 65
  lulus = [mahasiswa['nama']
    for mahasiswa in data
    if mahasiswa['nilai'] > 65]
  return lulus

# memanggil fungsi lulus untuk memberikan predikat lulus
# pada nama yang memiliki nilai lebih dari 65
hasil = predikatLulus(hasil_akhir)
print('mahasiswa yang lulus ialah', hasil)

#tugas2

buah = (['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])

def list_buah(buah):
    list_terbalik = []
    for i in range(len(buah)-1, -1, -1):
        list_terbalik.append(buah[i])
    return list_terbalik
hasil = list_buah(buah)
print('Hasilnya ada: ', hasil)

#nomor dua

list_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikasi(list_buah):
    list_baru = []
    for i in list_buah:
        list_baru.append([i, i])
    return list_baru

hasil_duplikasi = duplikasi(list_buah)
print(hasil_duplikasi)

#nomortiga

def konsonan(kalimat):
    huruf = ''

    for i in kalimat:
        if i not in 'aiueo':
            #menambahkan konsonan ke string kosong
            huruf += i
    return huruf 

#memanggil fungsi konsonan dengan string nurul fikri 
hasilnya = konsonan('Nurul Fikri')
print('huruf konsonan dari kata nurul fikri adalah', hasilnya)