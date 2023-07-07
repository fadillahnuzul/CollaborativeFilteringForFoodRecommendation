#untuk membuka dialog :
import tkinter as tk
from tkinter import *
from tkinter import ttk
from perhitungan_gizi import *
from main import *
import os
    
# def input_data_pengguna() :
class gui_data_input :
    global TINGGI, BERAT, USIA, JENIS_KELAMIN, AKTIVITAS, window

    window = tk.Tk()
    window.title("Input Data Pengguna")

    #input frame
    input_frame = ttk.Frame(window)
    input_frame.pack(padx=10,pady=10,fill="x",expand=True)
  
    #input tinggi badan
    TINGGI = tk.IntVar()
    BERAT = tk.IntVar()
    USIA = tk.IntVar()
    JENIS_KELAMIN = tk.IntVar()
    AKTIVITAS = tk.IntVar()
    tinggi_label = ttk.Label(input_frame,text="Input Tinggi Badan (cm)")
    tinggi_label.pack(padx=10,fill="x",expand=True)
    tinggi_entry = ttk.Entry(input_frame, textvariable=TINGGI)
    tinggi_entry.pack(padx=10,fill="x",expand=True)
    #input berat badan
    berat_label = ttk.Label(input_frame,text="Input Berat Badan (kg)")
    berat_label.pack(padx=10,fill="x",expand=True)
    berat_entry = ttk.Entry(input_frame, textvariable=BERAT)
    berat_entry.pack(padx=10,fill="x",expand=True)
    #input usia
    usia_label = ttk.Label(input_frame,text="Input Usia (tahun)")
    usia_label.pack(padx=10,fill="x",expand=True)
    usia_entry = ttk.Entry(input_frame, textvariable=USIA)
    usia_entry.pack(padx=10,fill="x",expand=True)
    #input jenis kelamin
    gender_label = ttk.Label(input_frame,text="Jenis kelamin : ")
    gender_label.pack(padx=10,pady=10,fill="x",expand=True)
    gender1 = Radiobutton(input_frame, text="Laki-laki", variable=JENIS_KELAMIN, value=1)
    gender1.pack( anchor = W )
    gender2 = Radiobutton(input_frame, text="Perempuan", variable=JENIS_KELAMIN, value=2)
    gender2.pack( anchor = W )
    #input jenis pekerjaan
    aktivitas_label = ttk.Label(input_frame,text="Jenis pekerjaan/aktivitas : ")
    aktivitas_label.pack(padx=10,pady=10,fill="x",expand=True)
    aktivitas1 = Radiobutton(input_frame, text="1. Ringan (75% duduk/berdiri, 25% berdiri/bergerak)", variable=AKTIVITAS, value=1)
    aktivitas1.pack( anchor = W )
    aktivitas2 = Radiobutton(input_frame, text="2. Sedang (25% duduk/berdiri, 75% berdiri/bergerak)", variable=AKTIVITAS, value=2)
    aktivitas2.pack( anchor = W )
    aktivitas3 = Radiobutton(input_frame, text="3. Berat (40% duduk/berdiri, 60% aktivitas)", variable=AKTIVITAS, value=3)
    aktivitas3.pack( anchor = W )
    #fungsi kirim data
    def send_data_user() :
        window.destroy()
        tinggi=TINGGI.get()
        berat=BERAT.get()
        usia=USIA.get()
        gender=JENIS_KELAMIN.get()
        aktivitas=AKTIVITAS.get()
        array_gizi, bmi = perhitungan_gizi_harian(tinggi,berat,usia,gender,aktivitas)
        hasil = main_fungsi(array_gizi, bmi)
        return array_gizi
    #button submit
    submit_button = ttk.Button(input_frame, text="Submit", command=send_data_user)
    submit_button.pack(padx=10,pady=10,fill="x",expand=True)
    
    window.mainloop()

# input_data_pengguna()