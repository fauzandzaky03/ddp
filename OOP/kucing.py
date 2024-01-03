class kucing:
    #atribut class
    nama = ''
    warna = ''
    umur = 0 

    #constructor
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    #method untuk menampilkan datanya 
    def data_kucing(self):
        print(f'nama kucing:{self.nama}')
        print(f'warna kucing:{self.warna}')
        print(f'umur kucing:{self.umur}')
