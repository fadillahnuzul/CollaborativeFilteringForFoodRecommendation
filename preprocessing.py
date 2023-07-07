def preprocessing(df) :
  #menghapus kolom serat
  df.drop(['serat'], axis = 1, inplace = True)
  #mendeteksi dan menghapus missing value
  print("Sebelum missing value dihilangkan :\n",df.isnull().sum())
  print("Ukuran data sebelum missing value dihilangkan :", df.shape)
  df = df.dropna(axis=0)
  print("Setelah missing value dihilangkan :\n",df.isnull().sum())
  df.reset_index(drop=True, inplace = True)
  print("Ukuran data setelah missing value dihilangkan :", df.shape)
  df.reset_index(drop=True, inplace = True)
  return df

def filter_lowfat(df, gizi) :
  df = df[df['lemak_per_porsi']<=gizi[3]]
  df.reset_index(drop=True, inplace = True)
  return df