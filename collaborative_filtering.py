import pandas as pd
import numpy as np
from scipy.spatial import distance
import random
from preprocessing import *

def get_disimilarity(kebutuhan_gizi:list, df_makanan:list) :
  vector_kebutuhan_gizi = np.array([kebutuhan_gizi[0],kebutuhan_gizi[1],kebutuhan_gizi[2]])
  matrix_disimilarity = [[[0] * len(df_makanan[2])] * len(df_makanan[1])] * len(df_makanan[0])
  #euclidean distance
  for i in range(len(df_makanan[0])) :
    for j in range(len(df_makanan[1])) :
      for k in range(len(df_makanan[2])) :
        data_resep_terpilih = np.array([df_makanan[0][i], df_makanan[1][j], df_makanan[2][k]])
        matrix_disimilarity[i][j][k] = np.linalg.norm(vector_kebutuhan_gizi - data_resep_terpilih)
  return matrix_disimilarity

def get_pembobotan(matrix_disimilarity, df_makanan:list) :
  n = 0.5
  maks_matrix = np.amax(matrix_disimilarity)
  matrix_bobot = [[[0] * len(df_makanan[2])] * len(df_makanan[1])] * len(df_makanan[0])
  for i in range(len(df_makanan[0])) :
    rating_sarapan = df_makanan[0]['rating']
    for j in range(len(df_makanan[1])) :
      rating_siang = df_makanan[1]['rating']
      for k in range(len(df_makanan[2])) :
        rating_malam = df_makanan[2]['rating']
        rating_rata_rata = (rating_sarapan + rating_siang + rating_malam)/3
        matrix_bobot[i][j][k] = n*(rating_rata_rata/5) + (1-n)*(1-((matrix_disimilarity[i][j][k])/maks_matrix))
  max_bobot = np.nanmax(matrix_bobot)
  index_max_bobot = np.argwhere(matrix_bobot == max_bobot)
  df_sarapan = pd.read_excel("DataUmami.xlsx", sheet_name='sarapan')
  df_sarapan = pd.DataFrame(df_sarapan)
  df_siang = pd.read_excel("DataUmami.xlsx", sheet_name='makan_siang')
  df_siang = pd.DataFrame(df_siang)
  df_malam = pd.read_excel("DataUmami.xlsx", sheet_name='makan_malam')
  df_malam = pd.DataFrame(df_malam)
  df_sarapan = preprocessing(df_sarapan)
  df_siang = preprocessing(df_siang)
  df_malam = preprocessing(df_malam)
  for i in range(1) :
    index_bobot_terpilih = random.choice(index_max_bobot)
    if (index_bobot_terpilih[1]>59 or index_bobot_terpilih[2]>73 or index_bobot_terpilih[3]>68) :
      index_bobot_terpilih = index_max_bobot[0]
    print(df_sarapan.loc[[index_bobot_terpilih[1]]])
    print(df_siang.loc[[index_bobot_terpilih[2]]])
    print(df_malam.loc[[index_bobot_terpilih[3]]])
    print("".center(60,"─"))
  return index_bobot_terpilih

def collab_filtering_camilan(df, gizi) :
  #euclidean distance
  a = gizi
  df['euclidean'] = np.nan
  for i in range (len(df)) :
    b = [df['kalori'][i], df['protein'][i], df['karbo'][i], df['lemak'][i]]
    b = b / df['sajian_per_resep'][i]
    df['euclidean'][i] = distance.euclidean(a,b)
  df = df.sort_values(['euclidean'], ascending=[True])
  #Pembobotan nutrisi dan rating
  n = 0.5
  max_jarak = max(df['euclidean'])
  for i in df :
    jarak = df['euclidean']
    rating = df['rating']
    df['score'] = n*(rating/5) + (1-n)*(1-(jarak/max_jarak))
  menu_rekomendasi = df.sort_values(['score'], ascending=[False]).head(7).sample(1)
  print(df.sort_values(['score'], ascending=[False]).head(7))
  return menu_rekomendasi

#menampilkan rekomendasi menu
def tampil_rekomendasi(rekomendasi, resep_bahan) :
  data_resep_bahan = pd.read_excel("DataUmami.xlsx", sheet_name=resep_bahan)
  inner_join = pd.merge(rekomendasi, data_resep_bahan, on ='nama_resep', how ='inner')
  show = inner_join[['nama_resep','bahan_bahan','cara_membuat','sajian_per_resep','kalori_per_porsi','rating']]
  return(np.array(show))
