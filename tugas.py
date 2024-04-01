print(10*'💀',"Ada Yang Kosong Ga Nich???",10*'💀')
ruang_kelas = {
    "D4.2": 25,
    "D4.3": 30,
    "D4.6": 35
}
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
ruang_tersedia = False
for ruang, kapasitas in ruang_kelas.items():
    if jumlah_mahasiswa <= kapasitas:
        print("Ruang kelas", ruang, "tersedia untuk", jumlah_mahasiswa, "mahasiswa😁")
        ruang_tersedia = True
        break
if not ruang_tersedia:
    print("Maaf, tidak ada ruang kelas yang tersedia untuk", jumlah_mahasiswa, "mahasiswa😢")