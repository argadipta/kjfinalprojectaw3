# 1. Input jumlah siswa
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# 2. Menyimpan semua data siswa dengan membuat list kosong
data_siswa = []

# 3. Input data siswa dengan looping
for i in range(jumlah_siswa):
    print(f"\nData siswa ke-{i+1}")
    nama = input("Nama siswa: ")
    nilai1 = float(input("Nilai Matematika: "))
    nilai2 = float(input("Nilai Coding: "))
    nilai3 = float(input("Nilai Bahasa Arab: "))
    
    rata_rata = (nilai1 + nilai2 + nilai3) / 3
    data_siswa.append({
        "nama": nama,
        "nilai": [nilai1, nilai2, nilai3],
        "rata_rata": rata_rata
    })

# 4. Membuat variable untuk Proses analisis
lulus = 0
tidak_lulus = 0

tertinggi = data_siswa[0]
terendah = data_siswa[0]

# 5. Analisis dan output data
print("\n--- Hasil Analisis ---")
for siswa in data_siswa:
    print(f"{siswa['nama']} - Rata-rata: {siswa['rata_rata']:.2f}")
    
    if siswa['rata_rata'] >= 75:
        lulus += 1
    else:
        tidak_lulus += 1
    
    if siswa['rata_rata'] > tertinggi['rata_rata']:
        tertinggi = siswa
    if siswa['rata_rata'] < terendah['rata_rata']:
        terendah = siswa

# 6. Menampilkan rekapitulasi hasil
print(f"\nJumlah siswa lulus: {lulus}")
print(f"Jumlah siswa tidak lulus: {tidak_lulus}")
print(f"Nilai tertinggi: {tertinggi['nama']} dengan {tertinggi['rata_rata']:.2f}")
print(f"Nilai terendah: {terendah['nama']} dengan {terendah['rata_rata']:.2f}")