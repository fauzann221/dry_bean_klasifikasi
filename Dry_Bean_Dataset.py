import pickle
import streamlit as st
import numpy as np

# Membaca model
model = pickle.load(open('Dry_Bean_Dataset.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

# Judul web
st.title('Prediksi Kategori Biji kering')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Area = st.number_input('Input nilai Area zona Biji Kering dan jumlah piksel di dalam batas-batasnya.')
    Perimeter = st.number_input('Input nilai Keliling Biji Kering didefinisikan sebagai panjang batasnya.')
    MajorAxisLength = st.number_input('Input nilai Jarak antara ujung garis terpanjang yang dapat ditarik dari sebuah bean.')
    MinorAxisLength = st.number_input('Input nilai Garis terpanjang yang bisa ditarik dari Biji Kering sambil berdiri tegak lurus pada sumbu utama.')
    AspectRation = st.number_input('Input nilai Menentukan hubungan antara L dan l')
    Eccentricity = st.number_input('Input nilai Eksentrisitas elips yang memiliki momen yang sama dengan wilayahnya.')

with col2:
    ConvexArea = st.number_input('Input nilai Jumlah piksel dalam poligon cembung terkecil yang dapat memuat area biji Biji Kering.')
    EquivDiameter = st.number_input('Input nilai Diameter lingkaran yang memiliki area yang sama dengan area biji Biji Kering.')
    Extent = st.number_input('Input nilai Rasio piksel dalam kotak pembatas terhadap area biji.')
    Solidity = st.number_input('Input nilai Rasio piksel dalam cangkang cembung dengan piksel yang ditemukan dalam biji.')
    roundness = st.number_input('Input nilai kebulatan biji kering')
    Compactness = st.number_input('Input nilai kepadatan biji kering')

# Code untuk prediksi
prediction = ''
input_data = (Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,
              Eccentricity,ConvexArea,EquivDiameter,Extent,Solidity,roundness,Compactness)

input_data_as_numpy_array = np.array(input_data)

input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshape)

# Membuat tombol untuk prediksi
if st.button('Test'):
    drybean_prediction = model.predict(std_data)
    if drybean_prediction[0] == 0:
        prediction = 'Tumbuhan Termasuk Kedalam Kelompok Barbuya'
    elif drybean_prediction[0] == 1:
        prediction = 'Tumbuhan Termasuk Kedalam Kelompok Bombay'
    elif drybean_prediction[0] == 2:
        prediction = 'Tumbuhan Termasuk Kedalam Kelompok Cali'
    elif drybean_prediction[0] == 3:
        prediction = 'Tumbuhan Termasuk Kedalam Kelompok Dermason'
    elif drybean_prediction[0] == 4:
        prediction = 'Tumbuhan Termasuk Kedalam Kelompok Horoz'
    elif drybean_prediction[0] == 5:
        prediction = 'Tumbuhan Termasuk Kedalam Kelompok Seker'
    else:
        prediction = 'Tumbuhan Termasuk Kedalam Kelompok Sira'
    
    st.success(prediction)