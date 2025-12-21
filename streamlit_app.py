import streamlit as st

st.title("Hello><")
st.write("Let's start record your finances!")
import streamlit as st
import pandas as pd
import os

st.title("💰 Aplikasi Manajemen Keuangan")

FILE_NAME = "data_keuangan.csv"

# Buat file jika belum ada
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Jenis", "Jumlah", "Keterangan"])
    df.to_csv(FILE_NAME, index=False)

# Load data
df = pd.read_csv(FILE_NAME)

menu = st.sidebar.selectbox(
    "Menu",
    ["Tambah Transaksi", "Riwayat Transaksi", "Saldo & Grafik"]
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

# ================= SALDO & GRAFIK =================
elif menu == "Saldo & Grafik":
    st.subheader("📊 Ringkasan Keuangan")

    pemasukan = df[df["Jenis"] == "Pemasukan"]["Jumlah"].sum()
    pengeluaran = df[df["Jenis"] == "Pengeluaran"]["Jumlah"].sum()
    saldo = pemasukan - pengeluaran

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Pemasukan", f"Rp {pemasukan}")
    col2.metric("Total Pengeluaran", f"Rp {pengeluaran}")
    col3.metric("Saldo Akhir", f"Rp {saldo}")

    st.divider()

    # ===== BAR CHART =====
    st.subheader("📊 Grafik Pemasukan vs Pengeluaran")
    chart_df = pd.DataFrame({
        "Kategori": ["Pemasukan", "Pengeluaran"],
        "Jumlah": [pemasukan, pengeluaran]
    })
    st.bar_chart(chart_df.set_index("Kategori"))

    # ===== LINE CHART =====
    st.subheader("📈 Tren Transaksi")
    if not df.empty:
        df["Index"] = range(1, len(df) + 1)
        st.line_chart(df.set_index("Index")["Jumlah"])
    else:
        st.info("Belum ada data untuk ditampilkan.")
