from dataclasses import dataclass

@dataclass
class Karyawan:
    id_karyawan: int
    nama: str
    jabatan: str
    gaji: float

daftar_karyawan = []

def tambah_karyawan():
    try:
        id_karyawan = int(input("Masukkan ID Karyawan: "))
        nama = input("Masukkan Nama Karyawan: ")
        jabatan = input("Masukkan Jabatan: ")
        gaji = float(input("Masukkan Gaji: "))
        karyawan = Karyawan(id_karyawan, nama, jabatan, gaji)
        daftar_karyawan.append(karyawan)
        print("Karyawan berhasil ditambahkan!\n")
    except ValueError:
        print("Input tidak valid. Pastikan ID dan Gaji berupa angka.")

def tampilkan_karyawan():
    if not daftar_karyawan:
        print("Belum ada data karyawan.\n")
    else:
        print("Daftar Karyawan:")
        print("="*40)
        for karyawan in daftar_karyawan:
            print(f"ID Karyawan : {karyawan.id_karyawan}")
            print(f"Nama        : {karyawan.nama}")
            print(f"Jabatan     : {karyawan.jabatan}")
            print(f"Gaji        : {karyawan.gaji}\n")
        print("="*40)

def cari_karyawan(id_karyawan):
    for karyawan in daftar_karyawan:
        if karyawan.id_karyawan == id_karyawan:
            return karyawan
    return None

def hapus_karyawan():
    try:
        id_karyawan = int(input("Masukkan ID Karyawan yang ingin dihapus: "))
        karyawan = cari_karyawan(id_karyawan)
        if karyawan:
            daftar_karyawan.remove(karyawan)
            print(f"Karyawan dengan ID {id_karyawan} berhasil dihapus.\n")
        else:
            print(f"Karyawan dengan ID {id_karyawan} tidak ditemukan.\n")
    except ValueError:
        print("Input tidak valid. Pastikan ID berupa angka.")

def menu():
    while True:
        print("Menu:")
        print("1. Tambah Karyawan")
        print("2. Tampilkan Semua Karyawan")
        print("3. Hapus Karyawan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            tampilkan_karyawan()
        elif pilihan == "3":
            hapus_karyawan()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")

# Menjalankan program
menu()
