import tkinter as tk

class Orang:

    def __init__(self, nama, tinggiBadan, beratBadan):
        self.nama = nama
        self.tinggiBadan = tinggiBadan
        self.beratBadan = beratBadan

    def gettinggiBadan(self):
        return self.tinggiBadan
    
    def getberatBadan(self):
        return self.beratBadan
    
    def getNama(self):
        return self.nama
    
    def settinggiSekarang(self, tinggiSekarang):
        self.tinggiBadan += tinggiSekarang

    def setberatSekarang(self, beratSekarang):
        self.beratBadan += beratSekarang

    def setNama(self, name):
        self.nama = name

    print("Kalkulator Menghitung Berat Badan Ideal")
    print("="*20)

dataAwal = Orang('Kosong',0,0)

if dataAwal.getNama() == 'Kosong':
    validasi = str(input('Ingin tau berat badan ya/tidak? '))
    if validasi == "ya":
        dataAwal.setNama(str(input("Masukan Nama : ")))
        dataAwal.setberatSekarang(int(input("Berapa Berat Anda : ")))
        dataAwal.settinggiSekarang(int(input("Berapa Tinggi Anda : ")))
    else:
        print("Silakan ketik 'ya' untuk mengetahui berat badan ideal Anda.")

    #rumus
    perhitungan = dataAwal.gettinggiBadan() - 100
    cariPersen = (10/100) * perhitungan
    nilaiAkhir = (perhitungan - cariPersen)

    print("="*20)
    print("Berat badan ideal kamu adalah", nilaiAkhir,"kg")
            
