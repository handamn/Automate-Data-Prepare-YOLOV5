import csv

def baca_file_csv(nama_file):
    data = []
    with open(nama_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        for baris in reader:
            data.append(baris[0])  # Ambil elemen pertama dari setiap baris
    return data

nama_file_csv = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/Out_line/Innova_RHD/Box1/index_kelas.csv'  # Ganti dengan nama file CSV Anda
data_csv = baca_file_csv(nama_file_csv)

val = input("Enter your value: ")

if val in data_csv:
    index = data_csv.index(val)
    print(f"{val} ditemukan pada indeks {index}")
    print(True)
    # Lakukan operasi lain berdasarkan indeks jika diperlukan
else:
    print(f"{val} tidak ditemukan dalam data_csv")
    print(False)
