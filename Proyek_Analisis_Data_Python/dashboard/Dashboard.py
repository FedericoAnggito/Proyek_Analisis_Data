import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca dataset

all_df = pd.read_csv("all_data.csv")

# Sidebar
st.sidebar.title("Pilih Opsi")
option = st.sidebar.selectbox("Pertanyaan Analisis", ["Pengaruh Cuaca", "Hubungan Kelembaban"])

# Main content
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Hello 👋")

# Visualisasi berdasarkan opsi yang dipilih
if option == "Pengaruh Cuaca":
    st.subheader("Pertanyaan 1 : Pengaruh Cuaca Terhadap Jumlah Peminjaman Sepeda")
    st.bar_chart(all_df.groupby('weathersit_x')['cnt_x'].sum())
    st.bar_chart(all_df.groupby('weathersit_y')['cnt_y'].sum())

elif option == "Hubungan Kelembaban":
    st.subheader("Pertanyaan 2 : Hubungan antara Kelembaban Udara dan Jumlah Peminjaman Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(x='hum_x', y='cnt_x', data=all_df, ax=ax)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.scatterplot(x='hum_y', y='cnt_y', data=all_df, ax=ax)
    st.pyplot(fig)

# Menambahkan keseluruhan dataset sebagai tabel di dashboard
st.subheader("Data Set Sepeda")
st.dataframe(all_df)

# Menampilkan tabel statistik ringkas
st.subheader("Statistik")
st.write(all_df.describe())