#pengurangan nutrisi nasi (180 kal, 3 gr protein, 39.8 gr karbo, 0.3 lemak)
def kurangi_nutrisi_nasi(df) :
  df[0] = df[0] - 180
  df[1] = df[1] - 3
  df[2] = df[2] - 39.8
  df[3] = df[3] - 0.3
  return df

#pengurangan nutrisi sayuran B (25 kal, 1 gr protein, 5 gr karbo)
def kurangi_nutrisi_sayur(df) :
  df[0] = df[0] - 25
  df[1] = df[1] - 1
  df[2] = df[2] - 5
  return df

#mengambil buah dan sayur secara acak
def random_buah_sayur(df) :
  df.sample()
  return df

#pengurangan nutrisi buah (50 kal, 12 gr karbo)
def kurangi_nutrisi_buah(df_nutrisi, df_buah) :
  df_buah = df_buah.to_numpy()
  df_nutrisi[0] = df_nutrisi[0] - df_buah[0][1]
  df_nutrisi[1] = df_nutrisi[1] - df_buah[0][2]
  df_nutrisi[2] = df_nutrisi[2] - df_buah[0][3]
  df_nutrisi[3] = df_nutrisi[3] - df_buah[0][4]
  return df_nutrisi