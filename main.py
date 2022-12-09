import pickle
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Interface import Jenis_Wisata
from Interface import Usia
from Interface import KategoriKunjungan
from Interface import Budget
from Interface import AkomodasiPenginapan
from Interface import Transportasi

# membaca model
model = pickle.load(open('model_ds.pkl', 'rb'))

# Rekomendasi Sistem
df_rec = pd.read_csv("Sumut_Go.csv")
df_rec = df_rec.drop(['Capwaktu','Usia','KategoriKunjungan','JenisWisata','Budget','AkomodasiPenginapan','Transportasi','TingkatKepuasanPengunjung'],axis = 1)

# Inisialisasi objek tfidf
tfidf = TfidfVectorizer(max_features=5000)

# Transform data
vectorized_data = tfidf.fit_transform(df_rec['DeskripsiSingkatPengalaman'].values)

vectorized_dataframe = pd.DataFrame(vectorized_data.toarray(), index=df_rec['DeskripsiSingkatPengalaman'].index.tolist())

similarity = cosine_similarity(vectorized_dataframe)

def recommendation(position):
    id_of_position = df_rec[df_rec['NamaWisata']==position].index[0]
    distances = similarity[id_of_position]
    position_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]
    
    for i in position_list:
       a = df_rec.iloc[i[0]].NamaWisata
    
   
    st.write(f'recomendation Wisata Lain: {a}', end='')


#judul web
st.title('Rekomendasi Wisata Sumatra Utara')

jeniswisata = st.selectbox('Pilih Jenis Wisata Yang Ingin Dikunjungi',
                           ('Wisata Alam','Wisata Kuliner','Wisata Religi','Wisata Sejarah dan Budaya'))
usia = st.selectbox('Usia Yang Akan Ikut Berkunjung',
                    ('Remaja','Dewasa','Anak-anak','Lansia'))
kategorikunjungan = st.selectbox('Jumlah Orang Yang Ikut Berkunjung',
                    ('Komunitas','Keluarga','Tunggal','Berdua'))
budget = st.selectbox('Budget Yang Sudah Disiapkan Dalam Kunjungan',
                    ('Low','Medium','High'))
akomodasipenginapan =st.selectbox('Akomodasi Penginapan Yang Dicari Saat Kunjungan',
                    ('Villa','Tidak Menginap','Hotel','Tenda','Kost'))
transportasi = st.selectbox('Kendaraan Yang Akan Digunakan Saat Kunjungan',
                    ('Bus','Motor','Mobil','Sepeda','Jalan Kaki'))


jeniswisata = Jenis_Wisata(jeniswisata)
usia = Usia(usia)
kategorikunjungan = KategoriKunjungan(kategorikunjungan)
budget = Budget(budget)
akomodasipenginapan = AkomodasiPenginapan(akomodasipenginapan)
transportasi = Transportasi(transportasi)

# initialize list of lists
data = [[jeniswisata,usia,kategorikunjungan,budget,akomodasipenginapan,transportasi]]
  
# Create the pandas DataFrame
New_Data = pd.DataFrame(data, columns=['Usia','KategoriKunjungan','JenisWisata','Budget','AkomodasiPenginapan','Transportasi'])

# Membuat Tombol
if st.button('Rekomendasi Wisata'):
    Prediction = model.predict(New_Data)
    pred = Prediction
    rec_str = pred.item()[:]

    # hasil prediksi
   
    st.write('Kunjungan Wisata yang Direkomendasiksan: ')
    st.write(rec_str)
    rec = recommendation(rec_str)
    