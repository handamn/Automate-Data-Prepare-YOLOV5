import os
import torch
import time
from tqdm import tqdm
import shutil
import random

out_or_in       = "Out_line"
nama_folder     = "4_ACDF" 
tipe_kendaraan  = "Innova_RHD"
box_ke          = "Box1"
basis_ke        = "train1"


folder_train_images = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/' + out_or_in + '/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder + '/images/'
folder_train_labels = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/' + out_or_in + '/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder + '/labels/'

folder_model = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/' + out_or_in + '/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder + '/models/' + basis_ke + '/weights/best.pt'

model = torch.hub.load('.', "custom", path = folder_model, source='local', force_reload=True)

direktori_class = "/home/pcsistem/camera_vision_develop/2_Stock_Foto/Out_line/Innova_RHD/Box1/index_kelas.txt"

with open(direktori_class, "r") as f:
    classes_list = [line.strip().replace("X_","") for line in f.readlines()]

# Mendapatkan daftar nama file di dalam folder
train_list = os.listdir(folder_train_images)

# Mencetak nama file di dalam folder
for nama in tqdm(train_list, desc="Processing Images"):

    # Membagi string menjadi list
    namafile = nama.split(".")

    # Mengambil string pertama
    namafile_clean = namafile[0]

    nama_file_txt = namafile_clean + ".txt"
    direktori_label = folder_train_labels + "/" + nama_file_txt
    #print(nama_file_txt)

    direktori_image = folder_train_images + "/" + nama
    results = model(direktori_image)
    hasil = results.pandas().xyxy[0]

    if (hasil.empty == False):
        xmin = hasil['xmin'][0]
        ymin = hasil['ymin'][0]
        xmax = hasil['xmax'][0]
        ymax = hasil['ymax'][0]
        kelas = hasil['class'][0]

        kelas_index = classes_list.index(str(nama_folder))

        xcenter = ((xmax+xmin)/2)/640
        ycenter = ((ymax+ymin)/2)/480
        width = (xmax-xmin)/640
        height = (ymax-ymin)/480


        text = str(kelas_index) + " " + str(xcenter) + " " + str(ycenter) + " " + str(width) + " " + str(height)

        with open(direktori_label, "w") as f:
            f.write(text)
        

        #bikin file class
        new_kelas = nama_folder[3:]
        nama_file_kelas_txt = "classes.txt"
        direktori_kelas = folder_train_labels + "/" + nama_file_kelas_txt

        """with open(direktori_kelas, "w") as f:
            f.write(new_kelas)"""
            
    else :
        os.remove(direktori_image)
        continue
    
    
print("ALHAMDULILLAH SELESAI")
print(" ")


###################################################


def split_data(input_folder, output_folder, split_ratio=0.8, random_seed=42):
    random.seed(random_seed)

    folder_gambar = os.path.join(input_folder, "images")
    folder_label = os.path.join(input_folder, "labels")

    folder_pelatihan = os.path.join(output_folder, "train")
    folder_gambar_pelatihan = os.path.join(folder_pelatihan, "images")
    folder_label_pelatihan = os.path.join(folder_pelatihan, "labels")

    folder_validasi = os.path.join(output_folder, "val")
    folder_gambar_validasi = os.path.join(folder_validasi, "images")
    folder_label_validasi = os.path.join(folder_validasi, "labels")

    # Buat folder keluaran jika belum ada
    for folder in [folder_pelatihan, folder_gambar_pelatihan, folder_label_pelatihan,
                   folder_validasi, folder_gambar_validasi, folder_label_validasi]:
        os.makedirs(folder, exist_ok=True)

    # Dapatkan daftar gambar di folder input
    daftar_gambar = os.listdir(folder_gambar)

    # Hitung jumlah gambar untuk pelatihan
    num_train = int(len(daftar_gambar) * split_ratio)

    # Acak daftar gambar
    random.shuffle(daftar_gambar)

    # Salin gambar dan label ke folder pelatihan
    for nama_gambar in daftar_gambar[:num_train]:
        path_gambar = os.path.join(folder_gambar, nama_gambar)
        path_label = os.path.join(folder_label, nama_gambar.replace(".jpg", ".txt"))

        shutil.copy(path_gambar, folder_gambar_pelatihan)
        shutil.copy(path_label, folder_label_pelatihan)

    # Salin gambar dan label ke folder validasi
    for nama_gambar in daftar_gambar[num_train:]:
        path_gambar = os.path.join(folder_gambar, nama_gambar)
        path_label = os.path.join(folder_label, nama_gambar.replace(".jpg", ".txt"))

        shutil.copy(path_gambar, folder_gambar_validasi)
        shutil.copy(path_label, folder_label_validasi)



folder_input = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/' + out_or_in + '/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder
folder_output = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/' + out_or_in + '/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder
split_data(folder_input, folder_output, split_ratio=0.8, random_seed=42)