# input
angka1 = float(input("masukan angka 1:"))
angka2 = float(input("masukan angka 2:"))
operator = input("pilih operator (+, -, *, /, **): ")

# proses
hasil = 0
if operator == "+":
    hasil = angka1 + angka2
    keterangan = "Tambah"
elif operator == "-":
    hasil = angka1 - angka2
    keterangan = "Kurang"
elif operator == "/":
    hasil = angka1 / angka2
    keterangan = "Bagi"
elif operator == "*":
    hasil = angka1 * angka2
    keterangan = "Kali"
elif operator == "**":
    hasil = angka1 ** angka2
    keterangan = "Pangkat"
else:
    print("operator tidak valid")
    exit()

#hasil
print(f"angka pertama: {angka1}")
print(f"angka kedua: {angka2}")
print(f"pilihan operator: {keterangan}")
print(f"hasil operator {angka1} {operator} {angka2} = {hasil}")

