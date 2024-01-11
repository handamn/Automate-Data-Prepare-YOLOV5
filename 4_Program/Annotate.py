import os
import torch
import pandas as pd
from tqdm import tqdm


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


folder_train_images = f'/home/pcsistem/camera_vision_develop/2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/images/'
folder_train_labels = f'/home/pcsistem/camera_vision_develop/2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/labels/'

folder_model = f'/home/pcsistem/camera_vision_develop/2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/Models/{model_ke}/weights/best.pt'

model = torch.hub.load('.', "custom", path=folder_model, source='local', force_reload=True)

direktori_class = "/home/pcsistem/camera_vision_develop/2_Stock_Foto/Out_line/Innova_RHD/Box1/index_kelas.csv"

# Membaca file kelas
kelas_df = pd.read_csv(direktori_class)
kelas_list = kelas_df.iloc[:, 0].tolist()

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
        data = {
            "class_index": [kelas_list.index(kode_box)],
            "xcenter": [((hasil['xmax'][0] + hasil['xmin'][0]) / 2) / 640],
            "ycenter": [((hasil['ymax'][0] + hasil['ymin'][0]) / 2) / 480],
            "width": [(hasil['xmax'][0] - hasil['xmin'][0]) / 640],
            "height": [(hasil['ymax'][0] - hasil['ymin'][0]) / 480],
        }

        # Menulis dataframe ke file CSV
        pd.DataFrame(data).to_csv(direktori_label, index=False)

        # Membuat dan menulis file kelas
        pd.DataFrame({"class_name": [kode_box[2:]]}).to_csv(
            os.path.join(folder_train_labels, "classes.csv"), index=False
        )

print("ALHAMDULILLAH SELESAI")
print(" ")
