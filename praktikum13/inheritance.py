class Manusia:
    def init(self, fnama, lname):
        self.fname = fnama
        self.lname = lname
        
    def cetak(self):
        print("Nama saya ",self.fname, self.lname)
        
class Staff(Manusia):
    def bekerja(self):
        print("Saya pekerja keras")
        
class Pelajar(Manusia):
    def init(self, fnama, lname, prodi, angkatan):
        super().init(fnama, lname)
        self.prodi = prodi
        self.angkatan = angkatan
        
    def cetak(self):
        super().cetak()
        print("Saya Mahasiswa Angkatan", self.angkatan, "di Program Studi", self.prodi)
        
    def belajar(self):
        print("Saya adalah pelajar")
        
# objek manusia
x = Manusia("Nada", "Indah")
x.cetak()

# objek staff
y = Staff("Dedi", "Drajat")
y.cetak()
y.bekerja()

# objek pelajar
danu = Pelajar("danu", "setiawan", "Sistem Informasi", 2023)
danu.cetak()
danu.belajar()