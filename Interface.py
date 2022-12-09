def Jenis_Wisata(JenisWisata):
  if JenisWisata == 'Wisata Alam':
    result = 0
  elif JenisWisata == 'Wisata Kuliner':
    result = 1
  elif JenisWisata == 'Wisata Religi':
    result = 2                
  elif JenisWisata == 'Wisata Sejarah dan Budaya':
    result = 3                             
  return result

def Usia(Usia):
  if Usia == 'Anak-anak':
    result = 0
  elif Usia == 'Remaja':
    result = 1
  elif Usia == 'Dewasa':
    result = 2                
  elif Usia == 'Lansia':
    result = 3                             
  return result

def KategoriKunjungan(KategoriKunjungan):
  if KategoriKunjungan == 'Komunitas':
    result = 0
  elif KategoriKunjungan == 'Keluarga':
    result = 1
  elif KategoriKunjungan == 'Tunggal':
    result = 2                
  elif KategoriKunjungan == 'Berdua':
    result = 3                             
  return result

def Budget(Budget):
  if Budget == 'Low':
    result = 0
  elif Budget == 'Medium':
    result = 1
  elif Budget == 'High':
    result = 2                                            
  return result

def AkomodasiPenginapan(AkomodasiPenginapan):
  if AkomodasiPenginapan == 'Villa':
    result = 0
  elif AkomodasiPenginapan == 'Tidak Menginap':
    result = 1
  elif AkomodasiPenginapan == 'Hotel':
    result = 2                
  elif AkomodasiPenginapan == 'Tenda':
    result = 3  
  elif AkomodasiPenginapan == 'Kost':
    result = 4                            
  return result

def Transportasi(transportasi):
  if transportasi == 'Bus':
    result = 0
  elif transportasi == 'Motor':
    result = 1
  elif transportasi == 'Mobil':
    result = 2                
  elif transportasi == 'Sepeda':
    result = 3  
  elif transportasi == 'Jalan Kaki':
    result = 4                            
  return result