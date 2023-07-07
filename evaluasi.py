import numpy as np
import pandas as pd
#Perhitungan kembali nutrisi nasi, sayur, dan buah
#Penambahan nutrisi nasi (180 kal, 3 gr protein, 39.8 gr karbo, 0.3 lemak)
def tambah_nutrisi_nasi(data_nutrisi) :
  data_nutrisi[0] = data_nutrisi[0] + 180
  data_nutrisi[1] = data_nutrisi[1] + 3
  data_nutrisi[2] = data_nutrisi[2] + 39.8
  data_nutrisi[3] = data_nutrisi[3] + 0.3
  return data_nutrisi

#Penambahan nutrisi sayuran B (25 kal, 1 gr protein, 5 gr karbo)
def tambah_nutrisi_sayur(data_nutrisi) :
  data_nutrisi[0] = data_nutrisi[0] + 25
  data_nutrisi[1] = data_nutrisi[1] + 1
  data_nutrisi[2] = data_nutrisi[2] + 5
  return data_nutrisi

#Penambahan nutrisi buah (50 kal, 12 gr karbo)
def tambah_nutrisi_buah(data_nutrisi, df_buah) :
  df_buah = df_buah.to_numpy()
  data_nutrisi[0] = data_nutrisi[0] + df_buah[0][1]
  data_nutrisi[1] = data_nutrisi[1] + df_buah[0][2]
  data_nutrisi[2] = data_nutrisi[2] + df_buah[0][3]
  data_nutrisi[3] = data_nutrisi[3] + df_buah[0][4]
  return data_nutrisi

def evaluasi(array_gizi, resep_rekomendasi:list, buah_rekomendasi:list) :
  gizi_resep = np.array([0,0,0,0])
  #Penambahan nutrisi nasi untuk 3x makan
  gizi_resep = tambah_nutrisi_nasi(gizi_resep)
  gizi_resep = tambah_nutrisi_nasi(gizi_resep)
  gizi_resep = tambah_nutrisi_nasi(gizi_resep)
  #Penambahan nutrisi sayur B
  gizi_resep = tambah_nutrisi_sayur(gizi_resep)
  gizi_resep = tambah_nutrisi_sayur(gizi_resep)
  print(gizi_resep)
  #Penambahan nutrisi buah
  for i in range(len(buah_rekomendasi)) :
    gizi_resep = tambah_nutrisi_buah(gizi_resep, buah_rekomendasi[i])
  print(gizi_resep)
  array_gizi = np.array(array_gizi)
  for i in range(len(resep_rekomendasi)) :
    gizi_resep[0] = gizi_resep[0] + resep_rekomendasi[i]['kalori_per_porsi']
    gizi_resep[1] = gizi_resep[1] + resep_rekomendasi[i]['protein_per_porsi']
    gizi_resep[2] = gizi_resep[2] + resep_rekomendasi[i]['karbo_per_porsi']
    gizi_resep[3] = gizi_resep[3] + resep_rekomendasi[i]['lemak_per_porsi']
  print("array_gizi yang dievaluasi",array_gizi)
  print("gizi_resep", gizi_resep)
  hasil_bagi = np.divide(gizi_resep, array_gizi)*100
  print("Kecukupan tiap gizi", hasil_bagi)
  # persentase_rata_rata = (np.mean(hasil_bagi))*100
  persentase_rata_rata = (gizi_resep[0]/array_gizi[0])*100
  return(persentase_rata_rata)