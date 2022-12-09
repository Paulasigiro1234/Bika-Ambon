# -*- coding: utf-8 -*-
"""Wisata Sumut PyCaret

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6B0VvtbwB3Jef9L3gYfemIKXZWmnsm7

# Initialization
"""

pip install pycaret

import pandas as pd

df = pd.read_csv("/content/Sumut_Go.csv")
df = df.drop(['Capwaktu','DeskripsiSingkatPengalaman','TingkatKepuasanPengunjung'],axis = 1)
# df = df.rename(columns={'Budget (Pengeluaran)': 'Budget'})
df.head()

df.drop(df[df['NamaWisata'] == "12. Roti Ganda Siantar"].index, inplace = True)
df.drop(df[df['NamaWisata'] == "18. Aek Sijorni Tapanuli Selatan"].index, inplace = True)
df.drop(df[df['NamaWisata'] == "23. Wisata Merci"].index, inplace = True)
df.drop(df[df['NamaWisata'] == "17. Aek Sipitu Dai Samosir"].index, inplace = True)

df['Usia'] = df['Usia'].map({'Remaja':0,'Dewasa':1,'Anak-anak':2,'Lansia':3})

df['KategoriKunjungan'] = df['KategoriKunjungan'].map({'Komunitas':0,'Keluarga':1,'Tunggal':2,'Berdua':3})

df['JenisWisata'] = df['JenisWisata'].map({'Wisata Alam':0,'Wisata Kuliner':1,'Wisata Religi':2,'Wisata Sejarah dan Budaya':3})

# df['NamaWisata'] = df['NamaWisata'].map({'18. Aek Sijorni Tapanuli Selatan':0,
#                                            '22. Pemandian Bah Damanik':1,
#                                            '3. Danau Toba':2,
#                                            '1. Air Terjun Ponot Kisaran':3,
#                                            '16. Pusuk Buhit Samosir':4,
#                                            '12. Roti Ganda Siantar':5,
#                                            '14. Bukit Sibea bea':6,
#                                            '2. Taman Wisata Iman Sidikalang':7,
#                                            '4. Mickey Holiday':8,
#                                            '6. Geosite Sipinsur':9,
#                                            '17. Aek Sipitu Dai Samosir':10,
#                                            '8. Landak River':11,
#                                            '11. Ucok Durian Medan':12,
#                                            '13. Menara Pandang Tele':13,
#                                            '23. Wisata Merci':14,
#                                            '5. Pasar Kamu Deli Serdang':15,
#                                            '21. Istana Maimun':16,
#                                            '9. Bukit Lawang':17,
#                                            '15. Pusat TB Silalahi (Museum Balige)':18})

df['Budget'] = df['Budget'].map({'Low':0,'Medium':1,'High':2})

df['AkomodasiPenginapan'] = df['AkomodasiPenginapan'].map({'Villa':0,'Tidak Menginap':1,'Hotel':2,'Tenda':3,'Kost':4})

df['Transportasi'] = df['Transportasi'].map({'Bus':0,'Motor':1,'Mobil':2,'Sepeda':3,'Jalan Kaki':4})


col = df.pop("NamaWisata")
df.insert(0, col.name, col)
df.head()

data_train = df.sample(frac=0.9, random_state=786)

data_test = df.drop(data_train.index)

"""# PyCaret"""

from pycaret.classification import *
from imblearn.over_sampling import RandomOverSampler

oversample = RandomOverSampler(random_state=42)
mclf = setup(data=data_train,
             target = "NamaWisata",
             fix_imbalance = True,
             fix_imbalance_method= oversample,
            #  fix_imbalance_method= imblearn.over_sampling.RandomOverSampler,
             remove_outliers = True,
             session_id=123)

best = compare_models()

dt = create_model("dt")

tuned_dt = tune_model(dt)

final_dt = finalize_model(tuned_dt)

test_pred = predict_model(final_dt, data= data_test)

test_pred

"""# Recommender System"""

df_rec = pd.read_csv("/content/Sumut_Go.csv")
df_rec = df_rec.drop(['Capwaktu','Usia','KategoriKunjungan','Budget','AkomodasiPenginapan','Transportasi','TingkatKepuasanPengunjung','DeskripsiSingkatPengalaman'],axis = 1)
df_rec

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi objek tfidf
tfidf = TfidfVectorizer(max_features=5000)

# Transform data
vectorized_data = tfidf.fit_transform(df_rec['JenisWisata'].values)

vectorized_data

vectorized_dataframe = pd.DataFrame(vectorized_data.toarray(), index=df_rec['JenisWisata'].index.tolist())

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectorized_dataframe)

def recommendation(position):
    id_of_position = df_rec[df_rec['NamaWisata']==position].index[0]
    distances = similarity[id_of_position]
    position_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]

    for i in position_list:
       a = df_rec.iloc[i[0]].NamaWisata


    print(f'recomendation Wisata Lain: {a}', end='')

"""# Interface Preparation"""

print('Unique Category: ', df_rec['JenisWisata'].nunique())
print( '\n', df_rec['Transportasi'].unique())

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

"""# User Interface"""

# input data baru
JenisWisata = 'Wisata Alam' #@param ['Wisata Alam','Wisata Kuliner','Wisata Religi','Wisata Sejarah dan Budaya']{type:"string"}
JenisWisata = Jenis_Wisata(JenisWisata)
Usia	 = 2 #@param [0,1,2,3]{type:"raw"}
KategoriKunjungan = 3 #@param [0,1,2,3]{type:"raw"}
Budget = 2 #@param [0,1,2]{type:"raw"}
AkomodasiPenginapan = 4 #@param [0,1,2,3,4]{type:"raw"}
Transportasi = 4#@param [0,1,2,3,4]{type:"raw"}



# initialize list of lists
data = [[Usia,KategoriKunjungan,JenisWisata,Budget,AkomodasiPenginapan,Transportasi]]

# Create the pandas DataFrame
New_Data = pd.DataFrame(data, columns=['Usia','KategoriKunjungan','JenisWisata','Budget','AkomodasiPenginapan','Transportasi'])

Prediction = predict_model(final_dt, data= New_Data)
pred = Prediction['Label'].values
rec_str = pred.item()[:]

# hasil prediksi
print("\n")
print(f'Kunjungan Wisata yang Direkomendasikan: {rec_str}', end='')
print("\n")
rec = recommendation(rec_str)

"""# Save Model"""

# save model untuk deploy
import joblib
import pickle

pickle.dump(tfidf, open('tfidf.sav', 'wb'))
pickle.dump(similarity, open('similarity.sav', 'wb'))
pickle.dump(final_dt, open('final_dt.sav', 'wb'))
pickle.dump(final_dt, open('final_dt.pkl', 'wb'))

save_model(final_dt,'gbc_Model')