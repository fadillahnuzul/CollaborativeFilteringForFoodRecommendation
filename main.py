import pandas as pd
import numpy as np
from tabulate import tabulate
from preprocessing import *
from perhitungan_gizi import *
from pengurangan_nutrisi import *
from collaborative_filtering import *
from evaluasi import *
from gui_data_output import *

#Membaca data
def main_fungsi(array_gizi, bmi) :
  print(bmi)
  print("====== Generate Rekomendasi ======")
  df_sarapan = pd.read_excel("DataUmami.xlsx", sheet_name='sarapan')
  df_sarapan = pd.DataFrame(df_sarapan)
  df_siang = pd.read_excel("DataUmami.xlsx", sheet_name='makan_siang')
  df_siang = pd.DataFrame(df_siang)
  df_malam = pd.read_excel("DataUmami.xlsx", sheet_name='makan_malam')
  df_malam = pd.DataFrame(df_malam)
  df_camilan = pd.read_excel("DataUmami.xlsx", sheet_name='camilan')
  df_camilan = pd.DataFrame(df_camilan)
  df_buah = pd.read_excel("DataBahanPenukar.xlsx", sheet_name='buah')
  df_buah = pd.DataFrame(df_buah)
  df_sayurA = pd.read_excel("DataBahanPenukar.xlsx", sheet_name='sayurA')
  df_sayurA = pd.DataFrame(df_sayurA)
  df_sayurB = pd.read_excel("DataBahanPenukar.xlsx", sheet_name='sayurB')
  df_sayurB = pd.DataFrame(df_sayurB)
  #Preprocessing data
  df_sarapan = preprocessing(df_sarapan)
  df_siang = preprocessing(df_siang)
  df_malam = preprocessing(df_malam)
  df_camilan = preprocessing(df_camilan)

    # array_gizi = input_data_pengguna()
    # Mengambil Input Data Pengguna

  #Pembagian gizi harian
  sarapan, siang, malam, camilan = [], [], [], []
  for i in range (len(array_gizi)) :
    sarapan.append(round(20/100*array_gizi[i], 3))
    siang.append(round(25/100*array_gizi[i], 3))
    malam.append(round(25/100*array_gizi[i], 3))
    camilan.append(round(10/100*array_gizi[i],3))
  
  #Filter lowfat pada pengguna gemuk
  if (bmi==4 or bmi==5) :
    df_sarapan = filter_lowfat(df_sarapan, sarapan)
    df_siang = filter_lowfat(df_siang, siang)
    df_malam = filter_lowfat(df_malam, malam)
    df_camilan = filter_lowfat(df_camilan, camilan)
  print(sarapan)
  print(df_sarapan)

  #Mengurangi nutrisi dengan nutrisi nasi pada menu makanan utama
  sarapan = kurangi_nutrisi_nasi(sarapan)
  siang = kurangi_nutrisi_nasi(siang)
  malam = kurangi_nutrisi_nasi(malam)
  #Mengurangi nutrisi dengan nutrisi sayuran B pada menu makanan utama
  sayur_pagi = df_sayurA.sample(1)
  sayurA_siang = df_sayurA.sample(1)
  sayurA_malam = df_sayurA.sample(1)
  sayurB_siang = df_sayurB.sample(1)
  sayurB_malam = df_sayurB.sample(1)
  siang = kurangi_nutrisi_sayur(siang)
  malam = kurangi_nutrisi_sayur(malam)
  #Mengurangi nutrisi dengan nutrisi buah pada menu makanan utama
  buah_siang = df_buah.sample(1)
  buah_malam = df_buah.sample(1)
  buah_camilan = df_buah.sample(1)
  siang = kurangi_nutrisi_buah(siang, buah_siang)
  malam = kurangi_nutrisi_buah(malam, buah_malam)
  camilan_pagi = kurangi_nutrisi_buah(camilan, buah_camilan)
  camilan_siang = kurangi_nutrisi_buah(camilan, buah_camilan)

  #collaborative filtering
  df_gizi_sarapan = df_sarapan.loc[:,['kalori_per_porsi','protein_per_porsi','karbo_per_porsi','lemak_per_porsi']].values.tolist()
  df_gizi_siang = df_siang.loc[:,['kalori_per_porsi','protein_per_porsi','karbo_per_porsi','lemak_per_porsi']].values.tolist()
  df_gizi_malam = df_malam.loc[:,['kalori_per_porsi','protein_per_porsi','karbo_per_porsi','lemak_per_porsi']].values.tolist()
  matrix_disimilarity = get_disimilarity([sarapan,siang,malam],[df_gizi_sarapan,df_gizi_siang,df_gizi_malam])
  index_resep_terpilih = np.array(get_pembobotan(matrix_disimilarity,[df_sarapan,df_siang,df_malam]))
  print(index_resep_terpilih)

  #Menentukan rekomendasi
  rekomendasi_sarapan = df_sarapan.loc[[index_resep_terpilih[1]]]
  rekomendasi_siang = df_siang.loc[[index_resep_terpilih[2]]]
  rekomendasi_malam = df_malam.loc[[index_resep_terpilih[3]]]
  rekomendasi_camilan_pagi = collab_filtering_camilan(df_camilan,camilan_pagi)
  rekomendasi_camilan_siang = collab_filtering_camilan(df_camilan,camilan_siang)
  rekomendasi_camilan_malam = collab_filtering_camilan(df_camilan,camilan)
  print(rekomendasi_sarapan, rekomendasi_siang, rekomendasi_malam)
  #Menampilkan rekomendasi
  tampil_sarapan = tampil_rekomendasi(rekomendasi_sarapan, 'sarapan_resep_bahan')
  tampil_siang = tampil_rekomendasi(rekomendasi_siang, 'makan_siang_resep_bahan')
  tampil_malam = tampil_rekomendasi(rekomendasi_malam, 'makan_malam_resep_bahan')
  tampil_camilan_pagi = tampil_rekomendasi(rekomendasi_camilan_pagi, 'camilan_resep_bahan')
  tampil_camilan_siang = tampil_rekomendasi(rekomendasi_camilan_siang, 'camilan_resep_bahan')
  tampil_camilan_malam = tampil_rekomendasi(rekomendasi_camilan_malam, 'camilan_resep_bahan')
  show_output([tampil_sarapan,tampil_siang, tampil_malam], "REKOMENDASI MENU MAKANAN UTAMA")
  show_output([tampil_camilan_pagi,tampil_camilan_siang, tampil_camilan_malam], "REKOMENDASI MENU CAMILAN")
  pd.describe_option('max_colwidth')
  print("\n\n\n################# SARAPAN ####################")
  print(tabulate(tampil_sarapan, headers='keys', tablefmt='pretty'))
  print("sayuran pagi:\n",sayur_pagi.nama_sayur.to_string(index=False)," sekehendak")
  print("\n\n\n################# CAMILAN PAGI ####################")
  print(tabulate(tampil_camilan_pagi, headers='keys', tablefmt='pretty'))
  print("buah camilan pagi:\n", buah_camilan.nama_buah.to_string(index=False), " ", buah_camilan.porsi_urt.to_string(index=False))
  print("\n\n\n################# MAKAN SIANG ####################")
  print(tabulate(tampil_siang, headers='keys', tablefmt='pretty'))
  print("sayuran siang:\n", sayurA_siang.nama_sayur.to_string(index=False)," sekehendak", "\n", sayurB_siang.nama_sayur.to_string(index=False)," 100 gram")
  print("buah siang:\n", buah_siang.nama_buah.to_string(index=False), " ", buah_siang.porsi_urt.to_string(index=False))
  print("\n\n\n################# CAMILAN SIANG ####################")
  print(tabulate(tampil_camilan_siang, headers='keys', tablefmt='pretty'))
  print("buah camilan siang:\n", buah_camilan.nama_buah.to_string(index=False), " ", buah_camilan.porsi_urt.to_string(index=False))
  print("\n\n\n################# MAKAN MALAM ####################")
  print(tabulate(tampil_malam, headers='keys', tablefmt='pretty'))
  print("sayuran malam:\n", sayurA_malam.nama_sayur.to_string(index=False)," sekehendak", "\n", sayurB_malam.nama_sayur.to_string(index=False)," 100 gram")
  print("buah malam:\n", buah_malam.nama_buah.to_string(index=False), " ", buah_malam.porsi_urt.to_string(index=False))
  print("\n\n\n################# CAMILAN MALAM ####################")
  print(tabulate(tampil_camilan_malam, headers='keys', tablefmt='pretty'))
      #Menentukan array gizi terbaru
    #Penambahan kembali nutrisi nasi, sayur, dan buah
    # array_gizi_baru = []
    # for i in range(len(array_gizi_lama)) :
    #   array_gizi_baru[i] = sarapan[i] + siang[i] + malam[i] + camilan_pagi[i] + camilan_siang[i] + camilan[i]
    # print("array_gizi baru", array_gizi_baru)

    #Evaluasi
  rekomendasi_buah = [buah_siang, buah_malam, buah_camilan, buah_camilan, buah_camilan]
  rekomendasi_menu = [rekomendasi_sarapan, rekomendasi_siang, rekomendasi_malam, rekomendasi_camilan_pagi, rekomendasi_camilan_siang, rekomendasi_camilan_malam]
  print("Rekomendasi menu ini dapat memenuhi kebutuhan nutrisi harian pengguna sebesar :")
  hasil_evaluasi = evaluasi(array_gizi, rekomendasi_menu, rekomendasi_buah)
  print(round(hasil_evaluasi,3),"%")


  sayur_pagi = np.array(df_sayurA.sample(1))
  sayurA_siang = np.array(df_sayurA.sample(1))
  sayurA_malam = np.array(df_sayurA.sample(1))
  sayurB_siang = np.array(df_sayurB.sample(1))
  sayurB_malam = np.array(df_sayurB.sample(1))
  buah_siang = np.array(buah_siang)
  buah_malam = np.array(buah_malam)
  buah_camilan = np.array(buah_camilan)
  show_output_pelengkap([sayur_pagi,sayurA_siang,sayurA_malam,sayurB_siang,sayurB_malam], [buah_siang,buah_malam,buah_camilan])