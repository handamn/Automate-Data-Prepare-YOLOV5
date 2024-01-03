import csv
import os
import torch
import time
from tqdm import tqdm
import shutil
import random

############################
out_or_in       = "Out_line"
nama_folder     = "4_ACDF" 
tipe_kendaraan  = "Innova_RHD"
box_ke          = "Box1"
basis_ke        = "train1"
############################

def baca_file_csv(nama_file):
    data = []
    with open(nama_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        for baris in reader:
            data.append(baris[0])  # Ambil elemen pertama dari setiap baris
    return data

def split_data(val, input_folder, output_folder, num_samples=200, split_ratio=0.8, random_seed=42):
    random.seed(random_seed)

    folder_gambar = os.path.join(input_folder, "images")
    folder_label = os.path.join(input_folder, "labels")

    gabung = os.path.join(output_folder, val)
    print(gabung)

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
folder_inline = base_folder + 'In_line/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder + '/'
folder_dummy = "/home/pcsistem/camera_vision_develop/4_Program/coba"
############################

val = input("Enter your value: ")

###outline_clean###

if val in data_csv:
    index = data_csv.index(val)
    print(f"{val} ditemukan pada indeks {index}")

    ##### Outline Clean #####
    for x in data_csv:
        if x != val :
            folder_outline_clean = base_folder + 'Out_line/' + tipe_kendaraan + '/' + box_ke + '/' + x

            folder_images_Outline = folder_outline_clean + 'images/'
            folder_labels_Outline = folder_outline_clean + 'labels/'
            split_data(val,folder_outline_clean, folder_dummy, num_samples=35, split_ratio=0.8, random_seed=42)
    ########################

    ##### Inline Clean #####
    folder_inline = base_folder + 'In_line/' + tipe_kendaraan + '/' + box_ke + '/' + val + '/'
    folder_images_Outline = folder_inline + 'images/'
    folder_labels_Outline = folder_inline + 'labels/'
    split_data(val,folder_inline, "/home/pcsistem/camera_vision_develop/4_Program/coba", num_samples=250, split_ratio=0.8, random_seed=42)
    ########################

    ##### Outline Clean #####
    folder_outline = base_folder + 'Out_line/' + tipe_kendaraan + '/' + box_ke + '/' + val + '/'
    folder_images_Outline = folder_outline + 'images/'
    folder_labels_Outline = folder_outline + 'labels/'
    split_data(val,folder_outline, "/home/pcsistem/camera_vision_develop/4_Program/coba", num_samples=250, split_ratio=0.8, random_seed=42)
    ########################


    print("ALHAMDULILLAH SELESAI")
    print(" ")


else:
    print(f"{val} tidak ditemukan dalam data_csv")
    print(False)


###inline###
"""
if val in data_csv:
    index = data_csv.index(val)
    print(f"{val} ditemukan pada indeks {index}")
    print(True)
    # Lakukan operasi lain berdasarkan indeks jika diperlukan
    ############################

    folder_outline = base_folder + 'In_line/' + tipe_kendaraan + '/' + box_ke + '/' + val + '/'


    folder_images_Outline = folder_outline + 'images/'
    folder_labels_Outline = folder_outline + 'labels/'


    # Mendapatkan daftar nama file di dalam folder
    image_list = os.listdir(folder_images_Outline)
    i = 0

    split_data(val,folder_outline, "/home/pcsistem/camera_vision_develop/4_Program/coba", num_samples=250, split_ratio=0.8, random_seed=42)

    print("ALHAMDULILLAH SELESAI")
    print(" ")


else:
    print(f"{val} tidak ditemukan dalam data_csv")
    print(False)


###outline###

if val in data_csv:
    index = data_csv.index(val)
    print(f"{val} ditemukan pada indeks {index}")
    print(True)
    # Lakukan operasi lain berdasarkan indeks jika diperlukan
    ############################

    folder_outline = base_folder + 'Out_line/' + tipe_kendaraan + '/' + box_ke + '/' + val + '/'


    folder_images_Outline = folder_outline + 'images/'
    folder_labels_Outline = folder_outline + 'labels/'


    # Mendapatkan daftar nama file di dalam folder
    image_list = os.listdir(folder_images_Outline)
    i = 0

    split_data(val,folder_outline, "/home/pcsistem/camera_vision_develop/4_Program/coba", num_samples=250, split_ratio=0.8, random_seed=42)

    print("ALHAMDULILLAH SELESAI")
    print(" ")


else:
    print(f"{val} tidak ditemukan dalam data_csv")
    print(False)"""