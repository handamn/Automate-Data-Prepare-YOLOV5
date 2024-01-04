import os
import torch
import time
from tqdm import tqdm
import shutil
import random

out_or_in       = "Out_line"
nama_folder     = "X_4_ACDF" 
tipe_kendaraan  = "Innova_RHD"
box_ke          = "Box1"
basis_ke        = "train1"


folder_train_images = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/' + out_or_in + '/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder + '/images/'
folder_train_labels = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/' + out_or_in + '/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder + '/labels/'

folder_model = '/home/pcsistem/camera_vision_develop/2_Stock_Foto/' + out_or_in + '/' + tipe_kendaraan + '/' + box_ke + '/' + nama_folder + '/models/' + basis_ke + '/weights/best.pt'

model = torch.hub.load('.', "custom", path = folder_model, source='local', force_reload=True)

direktori_class = "/home/pcsistem/camera_vision_develop/2_Stock_Foto/Out_line/Innova_RHD/Box1/list.txt"

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
        continue
    
    
    

print("ALHAMDULILLAH SELESAI")
print(" ")