import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Fungsi Keanggotaan
# ===============================

def rendah(x):
    if x <= 40:
        return 1
    elif 40 < x < 60:
        return (60 - x) / 20
    else:
        return 0


def sedang(x):
    if x <= 40 or x >= 80:
        return 0
    elif 40 < x <= 60:
        return (x - 40) / 20
    elif 60 < x < 80:
        return (80 - x) / 20


def tinggi(x):
    if x <= 60:
        return 0
    elif 60 < x < 80:
        return (x - 60) / 20
    else:
        return 1


# ===============================
# Interface Streamlit
# ===============================

st.title("📚 Sistem Penilaian Mahasiswa Menggunakan Logika Fuzzy")

nilai = st.slider(
    "Masukkan Nilai Ujian Mahasiswa",
    min_value=0,
    max_value=100,
    value=75
)

if st.button("Hitung"):

    # ===============================
    # Perhitungan Derajat Keanggotaan
    # ===============================
    mu_rendah = rendah(nilai)
    mu_sedang = sedang(nilai)
    mu_tinggi = tinggi(nilai)

    st.subheader("Derajat Keanggotaan")

    st.write(f"Rendah = {mu_rendah:.2f}")
    st.write(f"Sedang = {mu_sedang:.2f}")
    st.write(f"Tinggi = {mu_tinggi:.2f}")

    # ===============================
    # Penentuan Kategori
    # ===============================
    nilai_max = max(mu_rendah, mu_sedang, mu_tinggi)

    if nilai_max == mu_rendah:
        kategori = "Rendah"
    elif nilai_max == mu_sedang:
        kategori = "Sedang"
    else:
        kategori = "Tinggi"

    st.subheader("Kategori Akhir")
    st.success(f"Kategori Nilai Mahasiswa : {kategori}")

    # ===============================
    # Grafik Fungsi Keanggotaan
    # ===============================
    x = np.arange(0, 101, 1)

    y_rendah = [rendah(i) for i in x]
    y_sedang = [sedang(i) for i in x]
    y_tinggi = [tinggi(i) for i in x]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(x, y_rendah, 'b', linewidth=2, label='Rendah')
    ax.plot(x, y_sedang, 'g', linewidth=2, label='Sedang')
    ax.plot(x, y_tinggi, 'r', linewidth=2, label='Tinggi')

    # Garis vertikal nilai input
    ax.axvline(nilai, color='black', linestyle='--')

    # Titik derajat keanggotaan
    ax.plot(nilai, mu_rendah, 'bo')
    ax.plot(nilai, mu_sedang, 'go')
    ax.plot(nilai, mu_tinggi, 'ro')

    ax.set_xlabel("Nilai Ujian")
    ax.set_ylabel("μ(x)")
    ax.set_title("Grafik Fungsi Keanggotaan")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # ===============================
    # Interpretasi Hasil
    # ===============================
    st.subheader("Interpretasi Hasil")

    st.write(
        f"""
Nilai ujian **{nilai}** memiliki derajat keanggotaan:

- Rendah = **{mu_rendah:.2f}**
- Sedang = **{mu_sedang:.2f}**
- Tinggi = **{mu_tinggi:.2f}**

Karena derajat keanggotaan terbesar terdapat pada kategori **{kategori}**,
maka performa mahasiswa dikategorikan **{kategori}**.
"""
    )
