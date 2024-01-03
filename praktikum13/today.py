class animal:
    def __init__(self, name, makan, hidup, berkembangbiak):
        self.name = name
        self.makan = makan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak
    
    def info(self):
        print("Nama Hewan", self.name)
        print("Makannya", self.makan)
        print("Hidup di", self.hidup)
        print("Berkembangbiak di", self.berkembangbiak)
        print("============================")

class Badak (animal):
    def __init__(self, name, makan, hidup,berkembangbiak):
        super().__init__(name, makan, hidup, berkembangbiak)
        self.name = name
        self.makan = makan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak
Badak = Badak("Badak", "daun", "darat", "melahirkan")
Badak.info()

class Ikan (animal):
    def __init__(self, name, makan, hidup,berkembangbiak):
        super().__init__(name, makan, hidup, berkembangbiak)
        self.name = name
        self.makan = makan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak
Ikan = Ikan("Ikan", "Pelet", "Air", "Bertelur")
Ikan.info()

class Ular (animal):
    def _init_(self, name, makan, hidup,berkembangbiak):
        super().__init_
        _(name, makan, hidup, berkembangbiak)
        self.name = name
        self.makan = makan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak
Ular = Ular("Ular", "Daging", "Darat", "Bertelur")
Ular.info()