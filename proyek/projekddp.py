import tkinter as tk

def hitung_berat_ideal():
    berat = float(entry_berat.get())
    tinggi = float(entry_tinggi.get()) / 100
    
    jenis_kelamin = combo_jk.get()
    if jenis_kelamin == "Pria":
        berat_ideal = (tinggi * 100 - 100) - ((tinggi * 100 - 100) * 0.10)
    else:
        berat_ideal = (tinggi * 100 - 100) - ((tinggi * 100 - 100) * 0.15)
    
    label_hasil_ideal['text'] = f"Berat Badan Ideal: {berat_ideal:.2f} kg"

def clear_fields():
    entry_nama.delete(0, 'end')
    entry_umur.delete(0, 'end')
    entry_berat.delete(0, 'end')
    entry_tinggi.delete(0, 'end')
    label_hasil_ideal['text'] = ""

root = tk.Tk()
root.title("Kalkulator Berat Badan Ideal")
root.configure(bg='#bae2df')

frame = tk.Frame(root, padx="70", pady=30, bg='#bae2df')
frame.grid(row=0, column=0)

label_nama = tk.Label(frame, text="Nama:",padx=5, pady=5, bg='#bae2df')
label_nama.grid(row=0, column=0, sticky='w')

entry_nama = tk.Entry(frame, width=20)
entry_nama.grid(row=0, column=1)

label_umur = tk.Label(frame, text="Umur:",padx=5, pady=5, bg='#bae2df') 
label_umur.grid(row=1, column=0, sticky='w')

entry_umur = tk.Entry(frame, width=20)
entry_umur.grid(row=1, column=1)

label_berat = tk.Label(frame, text="Berat Badan (kg):",padx=5, pady=5,bg='#bae2df')  
label_berat.grid(row=2, column=0, sticky='w')

entry_berat = tk.Entry(frame, width=20)
entry_berat.grid(row=2, column=1)

label_tinggi = tk.Label(frame, text="Tinggi Badan (cm):",padx=5, pady=5, bg='#bae2df') 
label_tinggi.grid(row=3, column=0, sticky='w')

entry_tinggi = tk.Entry(frame, width=20)
entry_tinggi.grid(row=3, column=1)

label_jk = tk.Label(frame, text="Jenis Kelamin:",padx=5, pady=5, bg='#bae2df') 
label_jk.grid(row=4, column=0, sticky='w')

combo_jk = tk.StringVar()
combo_jk.set("Pria")  # Default value
dropdown = tk.OptionMenu(frame, combo_jk, "Pria", "Wanita")
dropdown.config(width=15)
dropdown.grid(row=4, column=1)

btn_hitung = tk.Button(frame, text="Hitung Berat Ideal", command=hitung_berat_ideal)
btn_hitung.grid(row=5, column=0, columnspan=2, pady=10)

btn_clear = tk.Button(frame, text="Clear", command=clear_fields)
btn_clear.grid(row=6, column=0, columnspan=2)

label_hasil_ideal = tk.Label(frame, text="",bg='#bae2df',fg='red')
label_hasil_ideal.grid(row=7, column=0, columnspan=2)

root.mainloop()