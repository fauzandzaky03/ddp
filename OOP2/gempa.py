class gempa:
    #atribut class
    lokasi = ""
    skala = 0

    #constructor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    #method untuk menampilkannya
    def data_gempa(self):
        if (self.skala < 2):
            ket = "gempa tidak berasa"
        elif (self.skala < 2 and self.skala > 4):
            ket = "gempa bangunan retak2"
        elif (self.skala < 4 and self.skala > 6):
            ket = "gempa bangunan roboh"
        elif (self.skala > 6):
            ket = "gempa bangunan roboh potensi tsunami"
        else:
            ket = "tidak diketahui"

        print(f"telah terjadi gempa, {self.lokasi}, dengan skala, {self.skala}, {ket}")

   



    
