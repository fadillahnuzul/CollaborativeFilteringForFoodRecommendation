def perhitungan_gizi_harian(tinggi, berat, usia, jenis_kelamin, jenis_kerja) :
  global energi,bmi_kategori
  #Input data
  # tinggi = int(input("Input tinggi badan (dalam cm) : "))
  # berat = int(input("Input berat badan (dalam kg) : "))
  # usia = int(input("Input usia (dalam tahun) : "))
  # jenis_kelamin = input("Input jenis kelamin (L/P) : ")
  # jenis_kerja = input("Jenis pekerjaan \n1.Ringan (75% duduk/berdiri, 25% berdiri/bergerak) \n2.Sedang (25% duduk/berdiri, 75% berdiri/bergerak) \n3.Berat (40% duduk/berdiri, 60% aktivitas) \nInput jenis pekerjaan (1/2/3) : ")

  #Perhitungan energi harian
  if jenis_kelamin == 1 :
    BMR = 66 + (13.7*berat) + (5*tinggi) - (6.8*usia)
    if jenis_kerja == 1 :
      energi = BMR*1.56
    elif jenis_kerja == 2 :
      energi = BMR*1.76
    elif jenis_kerja == 3 :
      energi = BMR*2.1
  elif jenis_kelamin == 2 :
    BMR = 665 + (9.6*berat) + (1.8*tinggi) - (4.7*usia)
    if jenis_kerja == 1 :
      energi = BMR*1.55
    elif jenis_kerja == 2 :
      energi = BMR*1.7
    elif jenis_kerja == 3 :
      energi = BMR*2
  
  #Menghitung BMI
  bmi = berat/((tinggi/100)**2)
  if bmi < 17 :
    bmi_kategori = 1
    bmi_kategori_text = "Kurus (kekurangan berat badan tingkat berat)"
    energi = energi + 500
  elif 17 <= bmi < 18.5 :
    bmi_kategori = 2
    bmi_kategori_text = "Kurus (kekurangan berat badan tingkat ringan)"
    energi = energi + 500
  elif 18.5 <= bmi <= 25 :
    bmi_kategori = 3
    bmi_kategori_text = "Normal"
  elif 25 < bmi <= 27 :
    bmi_kategori = 4
    bmi_kategori_text = "Gemuk (kelebihan berat badan tingkat ringan)"
    energi = energi - 500
  elif bmi > 27 :
    bmi_kategori = 5
    bmi_kategori_text = "Gemuk (kelebihan berat badan tingkat berat)"
    energi = energi - 500
  print(bmi_kategori_text)
  energi = round(energi, 3)
  #perhitungan protein, karbohidrat, lemak
  protein = round((12/100*energi)/4, 3)
  karbo = round((68/100*energi)/4, 3)
  lemak = round((20/100*energi)/9, 3)
  array_gizi = [energi, protein, karbo, lemak] #kalori dibuat perhari
  print(array_gizi)
  return (array_gizi, bmi_kategori)