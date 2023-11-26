#deklarasi
def profil(nama, alamat, gender, umur, hobi):
    print("nama:", nama)
    print("alamat:", alamat)
    print("gender:", gender)
    print("umur:", umur)
    print("hobi:", hobi)

profil("Fauzan", "Jln Alfalah", "Laki-Laki", 18, "Futsal")

#nomordua

def cek_kelulusan(nilai):
    if nilai < 60:
        return "gagal"
    elif 60 <= nilai <= 70:
        return "baik"
    elif 71 <= nilai <= 80:
        return "sangat baik"
    elif 80 <= nilai <= 100:
        return "istimewa"
    else:
        return "Nilai tidak valid"
    
nilai = 80
hasil = cek_kelulusan(nilai)
print(f"nilai {nilai} {hasil}")
    



#nomortiga

def ganjil(n):
    for i in range(1, n+1, 2):
        print(i)
ganjil(100)