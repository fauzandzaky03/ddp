

def persegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi

    print("luasnya adalah", luas)
    print("kelilingnya adalah", keliling)


def persegi_panjang(panjang,lebar):
    luas = panjang * lebar
    keliling = 2*(panjang+lebar)

    print("luasnya adalah", luas)
    print("kelilingnya adalah", keliling)

def lingkaran(pi,jari_jari):
    luas = pi * (jari_jari ** 2)
    keliling = 2 * pi * jari_jari

    print("luasnya adalah", luas)
    print("kelilingnya adalah", keliling)


def segitiga(alas,tinggi,sisi_miring):
    luas = 0.5 * alas * tinggi
    keliling =  alas + sisi_miring + sisi_miring

    print("luasnya adalah", luas)
    print("kelilingnya adalah", keliling)

def jajar_genjang(alas_jajar_genjang,sisi_miring_jajar_genjang,tinggi_jajar_genjang):
    luas = alas_jajar_genjang * tinggi_jajar_genjang
    keliling =  2 * (alas_jajar_genjang + sisi_miring_jajar_genjang)

    print("luasnya adalah", luas)
    print("kelilingnya adalah", keliling)

def trapesium(sisi_a,sisi_b,tinggi_trapesium,sisi_miring_trapesium):
    luas = 0.5 * (sisi_a + sisi_b) * tinggi_trapesium
    keliling =  sisi_a + sisi_b + tinggi_trapesium + sisi_miring_trapesium

    print("luasnya adalah", luas)
    print("kelilingnya adalah", keliling)

def belah_ketupat(diagonal_1,diagonal_2):
    luas =  0.5 * diagonal_1 * diagonal_2
    keliling =  4 * diagonal_1

    print("luasnya adalah", luas)
    print("kelilingnya adalah", keliling)















