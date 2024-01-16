import os
import torch
import pandas as pd
from tqdm import tqdm

#####################
basis_folder = "/home/pcsistem/camera_vision_develop/"
#####################

############################
print(" ")
out_or_in  = input("Enter Lini Produksi            (ex : Out_line : ")
car        = input("Enter Car Model                (ex : Innova)  : ")
steer      = input("Enter Steer                    (ex : RHD)     : ")
box        = input("Enter Box Class                (ex : Box1)    : ")
kode_box   = input("Enter Code Box                 (ex : X_3_CDE) : ")
model_ke   = input("Enter Model Train              (ex : train1)  : ")

print(" ")
kendaraan  = car + "_" + steer
############################


folder_train_images = f'{basis_folder}/2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/images/'
folder_train_labels = f'{basis_folder}/2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/labels/'

os.makedirs(folder_train_labels, exist_ok = True)

folder_model = f'{basis_folder}/2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/Models/{model_ke}/weights/best.pt'

model = torch.hub.load('.', "custom", path=folder_model, source='local', force_reload=True)


# Mendapatkan daftar nama file di dalam folder
train_list = os.listdir(folder_train_images)

# Mencetak nama file di dalam folder
for nama in tqdm(train_list, desc="Processing Images"):

    # Membuat nama file label
    nama_file_label = f"{nama.split('.')[0]}.txt"
    direktori_label = os.path.join(folder_train_labels, nama_file_label)

    direktori_image = os.path.join(folder_train_images, nama)
    results = model(direktori_image)
    hasil = results.pandas().xyxy[0]

    if not hasil.empty:
        xmin = hasil['xmin'][0]
        ymin = hasil['ymin'][0]
        xmax = hasil['xmax'][0]
        ymax = hasil['ymax'][0]
        kelas = hasil['class'][0]

        kelas_index = 0

        xcenter = ((xmax+xmin)/2)/640
        ycenter = ((ymax+ymin)/2)/480
        width = (xmax-xmin)/640
        height = (ymax-ymin)/480


        text = str(kelas_index) + " " + str(xcenter) + " " + str(ycenter) + " " + str(width) + " " + str(height)

        with open(direktori_label, "w") as f:
            f.write(text)

with open(f"{folder_train_labels}/classes.txt", "w") as f:
    f.write(kode_box)

print("ALHAMDULILLAH SELESAI")
print(" ")
