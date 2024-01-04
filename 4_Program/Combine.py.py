import csv
import os
import torch
import time
from tqdm import tqdm
import shutil
import random

############################
print(" ")
car        = input("Enter Car Model                (ex : Innova)  : ")
steer      = input("Enter Steer                    (ex : RHD)     : ")
box        = input("Enter Box Class                (ex : Box1)    : ")
kode_box   = input("Enter Code Box                 (ex : X_3_CDE) : ")
kendaraan  = car + "_" + steer

OK_count   = int(input("Enter OK Value                 (ex : 200)     : "))
NG_count   = int(input("Enter NG Value each folder     (ex : 35)      : "))
percentage = input("Enter OK Percentage            (ex: 80)       : ")
percentage = int(percentage) / 100
############################

def baca_file_csv(nama_file):
    data = []
    with open(nama_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        for baris in reader:
            data.append(baris[0])  # Ambil elemen pertama dari setiap baris
    return data

def split_data(kode_box, input_folder, output_folder, num_samples=200, split_ratio=0.8, random_seed=42):
    random.seed(random_seed)

    folder_gambar = os.path.join(input_folder, "images")
    folder_label = os.path.join(input_folder, "labels")

    gabung = os.path.join(output_folder, kode_box)

    folder_pelatihan = os.path.join(gabung, "train")
    folder_gambar_pelatihan = os.path.join(folder_pelatihan, "images")
    folder_label_pelatihan = os.path.join(folder_pelatihan, "labels")

    folder_validasi = os.path.join(gabung, "val")
    folder_gambar_validasi = os.path.join(folder_validasi, "images")
    folder_label_validasi = os.path.join(folder_validasi, "labels")

    # Buat folder keluaran jika belum ada
    for folder in [folder_pelatihan, folder_gambar_pelatihan, folder_label_pelatihan,
                   folder_validasi, folder_gambar_validasi, folder_label_validasi]:
        os.makedirs(folder, exist_ok=True)

    # Dapatkan daftar gambar di folder input
    daftar_gambar = os.listdir(folder_gambar)

    # Ambil secara acak 200 sampel
    sampled_images = random.sample(daftar_gambar, num_samples)

    # Hitung jumlah gambar untuk pelatihan
    num_train = int(len(sampled_images) * split_ratio)

    # Salin gambar dan label ke folder pelatihan
    with tqdm(total=num_train, desc="Copying training data") as pbar:
        for nama_gambar in sampled_images[:num_train]:
            path_gambar = os.path.join(folder_gambar, nama_gambar)
            path_label = os.path.join(folder_label, nama_gambar.replace(".jpg", ".txt"))

            shutil.copy(path_gambar, folder_gambar_pelatihan)
            shutil.copy(path_label, folder_label_pelatihan)

            pbar.update(1)

    # Salin gambar dan label ke folder validasi
    with tqdm(total=len(sampled_images) - num_train, desc="Copying validation data") as pbar:
        for nama_gambar in sampled_images[num_train:]:
            path_gambar = os.path.join(folder_gambar, nama_gambar)
            path_label = os.path.join(folder_label, nama_gambar.replace(".jpg", ".txt"))

            shutil.copy(path_gambar, folder_gambar_validasi)
            shutil.copy(path_label, folder_label_validasi)

            pbar.update(1)


nama_file_csv = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/Out_line/Innova_RHD/Box1/index_kelas.csv'  # Ganti dengan nama file CSV Anda
data_csv = baca_file_csv(nama_file_csv)

############################
base_folder = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/'
folder_output = "/home/pcsistem/camera_vision_develop/5_STUDIO_MAKER/Innova_RHD/Box1"
############################

i = 0

###outline_clean###

if kode_box in data_csv:
    index = data_csv.index(kode_box)
    print(f"{kode_box} ditemukan pada indeks {index}")

    ##### Outline Clean #####
    for x in data_csv:
        if x != kode_box :
            i+=1
            folder_outline_clean = base_folder + 'Out_line/' + kendaraan + '/' + box + '/' + x
            split_data(kode_box,folder_outline_clean, folder_output, num_samples=NG_count, split_ratio=percentage, random_seed=42)
    ########################

    ##### Inline Clean #####
    folder_inline = base_folder + 'In_line/' + kendaraan + '/' + box + '/' + kode_box + '/'
    split_data(kode_box,folder_inline, folder_output, num_samples=OK_count, split_ratio=percentage, random_seed=42)
    ########################

    ##### Outline Clean #####
    folder_outline = base_folder + 'Out_line/' + kendaraan + '/' + box + '/' + kode_box + '/'
    split_data(kode_box,folder_outline, folder_output, num_samples=OK_count, split_ratio=percentage, random_seed=42)
    ########################

    print(" ")
    print(" ")
    print("#################################################")
    print(" ")
    print(f"DATA TRAINING {kode_box}")
    print(" ")
    print("=====BERHASIL DIBUAT=====")
    print(" ")
    print(f"Perbandingan Data Benar : {OK_count*2} dengan Data Salah : {NG_count*i}")
    print(" ")
    print(f"Rasio Pesebaran Data {percentage}")
    print(" ")
    print(f"Total Data yang Dibuat : {(OK_count*2)+(NG_count*i)}")
    print(" ")
    print("#################################################")




else:
    print(f"{kode_box} tidak ditemukan dalam data_csv")
    print(False)

