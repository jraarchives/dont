import streamlit as st

st.title("Hello><")
st.write("Let's start record your finances!")
import streamlit as st
import pandas as pd
import os

st.title("Keuanganku")

FILE_NAME = "data_keuangan.csv"

# Jika file belum ada, buat dulu
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Jenis", "Jumlah", "Keterangan"])
    df.to_csv(FILE_NAME, index=False)

# Load data
df = pd.read_csv(FILE_NAME)

# Menu
menu = st.sidebar.selectbox(
    "Menu",
    ["Tambah Transaksi", "Riwayat Transaksi", "Saldo"]
)

# ================= TAMBAH TRANSAKSI =================
if menu == "Tambah Transaksi":
    st.subheader("➕ Tambah Transaksi")

    jenis = st.selectbox("Jenis Transaksi", ["Pemasukan", "Pengeluaran"])
    jumlah = st.number_input("Jumlah (Rp)", min_value=0)
    keterangan = st.text_input("Keterangan")

    if st.button("Simpan"):
        data_baru = {
            "Jenis": jenis,
            "Jumlah": jumlah,
            "Keterangan": keterangan
        }
        df = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)
        df.to_csv(FILE_NAME, index=False)
        st.success("Transaksi berhasil disimpan!")

# ================= RIWAYAT =================
elif menu == "Riwayat Transaksi":
    st.subheader("📋 Riwayat Transaksi")
    st.dataframe(df)

# ================= SALDO =================
elif menu == "Saldo":
    st.subheader("📊 Saldo Keuangan")

    pemasukan = df[df["Jenis"] == "Pemasukan"]["Jumlah"].sum()
    pengeluaran = df[df["Jenis"] == "Pengeluaran"]["Jumlah"].sum()
    saldo = pemasukan - pengeluaran

    st.write(f"**Total Pemasukan:** Rp {pemasukan}")
    st.write(f"**Total Pengeluaran:** Rp {pengeluaran}")
    st.write(f"### 💵 Saldo Akhir: Rp {saldo}")
