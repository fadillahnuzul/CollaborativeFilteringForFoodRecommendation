#untuk membuka dialog :
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
from collaborative_filtering import *
from tkinter.font import Font
import numpy as np
    
def show_output(hasil_rekomendasi:list, judul) :
    window = tk.Tk()
    window.title("Hasil Rekomendasi")
    window.geometry("1800x720")
    window.title(judul)

    output_frame = Frame(window)
    output_frame.pack(padx=15,pady=15)

    label = Label(output_frame, text=judul)
    label.pack(side=TOP)

    tv = ttk.Treeview(output_frame, columns=(1,2,3,4,5,6), show="headings")
    tv.heading(1,text="Nama Resep")
    tv.heading(2,text="Bahan-bahan")
    tv.heading(3,text="Cara Membuat")
    tv.heading(4,text="Sajian/resep")
    tv.heading(5,text="Kalori/sajian")
    tv.heading(6,text="Rating")
    tv.column(1,width=200 ,stretch=YES)
    tv.column(2,width=300,stretch=YES)
    tv.column(3,width=700,stretch=YES)
    tv.column(4,width=100,stretch=YES)
    tv.column(5,width=100,stretch=YES)
    tv.column(6,width=100,stretch=YES)
    tv.pack(fill=BOTH,expand=0, side=TOP)

    sb = Scrollbar(window, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)

    tv.config(yscrollcommand=sb.set)
    sb.config(command=tv.yview)

    font = Font(family='Arial', size=300)  # use whatever font you like
    line_height = font.metrics()['linespace']  # returns an integer
    # set Treeview row height based on font size
    style = ttk.Style()
    style.configure('Treeview', rowheight=line_height)

    for i in range (len(hasil_rekomendasi)) :
        tv.insert('','end',text=hasil_rekomendasi[i][0][0],values=(hasil_rekomendasi[i][0][0],hasil_rekomendasi[i][0][1],hasil_rekomendasi[i][0][2],hasil_rekomendasi[i][0][3],hasil_rekomendasi[i][0][4],hasil_rekomendasi[i][0][5]))

    window.mainloop()

def show_output_pelengkap(array_sayur:list, array_buah:list) :
    window = tk.Tk()
    window.title("Hasil Rekomendasi")
    window.geometry("600x600")
    window.title("REKOMENDASI PELENGKAP (SAYUR & BUAH)")

    output_frame = Frame(window)
    output_frame.pack(padx=15,pady=15)

    label = Label(output_frame, text="REKOMENDASI PELENGKAP (SAYUR & BUAH)\n", font="arial 12 bold")
    label.pack(side=TOP)
    #sarapan
    label_sarapan = Label(output_frame, text="\nRekomendasi Buah dan Sayur Sarapan", font="arial 10 bold")
    label_sarapan.pack()
    label_sarapan = Label(output_frame, text=array_sayur[0][0][0]+" secukupnya", font="arial 10")
    label_sarapan.pack()
    #camilan pagi
    label_snack_pagi = Label(output_frame, text="\nRekomendasi Buah Camilan Pagi", font="arial 10 bold")
    label_snack_pagi.pack()
    label_snack_pagi = Label(output_frame, text=array_buah[2][0][0]+" "+array_buah[2][0][6], font="arial 10")
    label_snack_pagi.pack()
    #makan siang
    label_makan_siang = Label(output_frame, text="\nRekomendasi Buah dan Sayur Makan Siang", font="arial 10 bold")
    label_makan_siang.pack()
    label_sayura_siang = Label(output_frame, text=array_sayur[1][0][0]+" secukupnya", font="arial 10")
    label_sayura_siang.pack()
    label_sayurb_siang = Label(output_frame, text=array_sayur[3][0][0]+" 100 gram", font="arial 10")
    label_sayurb_siang.pack()
    label_buah_siang = Label(output_frame, text=array_buah[0][0][0]+" "+array_buah[0][0][6], font="arial 10")
    label_buah_siang.pack()
    #camilan siang
    label_snack_siang = Label(output_frame, text="\nRekomendasi Buah Camilan Siang", font="arial 10 bold")
    label_snack_siang.pack()
    label_snack_siang = Label(output_frame, text=array_buah[2][0][0]+" "+array_buah[2][0][6], font="arial 10")
    label_snack_siang.pack()
    #makan malam
    label_makan_malam = Label(output_frame, text="\nRekomendasi Buah dan Sayur Makan Malam", font="arial 10 bold")
    label_makan_malam.pack()
    label_sayura_malam = Label(output_frame, text=array_sayur[2][0][0]+" secukupnya", font="arial 10")
    label_sayura_malam.pack()
    label_sayurb_malam = Label(output_frame, text=array_sayur[4][0][0]+" 100 gram", font="arial 10")
    label_sayurb_malam.pack()
    label_buah_malam = Label(output_frame, text=array_buah[1][0][0]+" "+array_buah[1][0][6], font="arial 10")
    label_buah_malam.pack()
    #camilan malam
    label_snack_siang = Label(output_frame, text="\nRekomendasi Buah Camilan Malam", font="arial 10 bold")
    label_snack_siang.pack()
    label_snack_siang = Label(output_frame, text=array_buah[2][0][0]+" "+array_buah[2][0][6], font="arial 10")
    label_snack_siang.pack()

    window.mainloop()