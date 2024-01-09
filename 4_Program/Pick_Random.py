import os
import random
import shutil
import yaml

def copy_random_images(source_folder, destination_folder, num_images):
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png','.jpg','.jpeg'))]
    num_images = min(num_images,len(image_files))
    random_images = random.sample(image_files, num_images)

    for image in random_images:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        shutil.copy2(source_path, destination_path)
        print(f"Copied: {image}")


############################
print(" ")
out_or_in     = input("Enter Lini Produksi            (ex : Out_line : ")
car           = input("Enter Car Model                (ex : Innova)  : ")
steer         = input("Enter Steer                    (ex : RHD)     : ")
box           = input("Enter Box Class                (ex : Box1)    : ")
kode_box      = input("Enter Code Box                 (ex : X_3_CDE) : ")
jumlah_gambar = input("Enter How Many Image           (ex : 100)     : ")

print(" ")
kendaraan  = car + "_" + steer
############################

source_folder = f'/home/pcsistem/camera_vision_develop/2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/images/'

automasi_folder = f'/home/pcsistem/camera_vision_develop/2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/X_Automasi/'
sub_automasi_images_folder = os.path.join(automasi_folder, 'images')
sub_automasi_labels_folder = os.path.join(automasi_folder, 'labels')

for folder in [automasi_folder, sub_automasi_images_folder, sub_automasi_labels_folder]:
    os.makedirs(folder, exist_ok=True)

destination_folder = sub_automasi_images_folder

copy_random_images(source_folder, destination_folder, int(jumlah_gambar))


data = {
    'train': automasi_folder,
    'val': automasi_folder,
    'names': {
        0: kode_box
    }
}

file_path = automasi_folder + kode_box +'.yaml'  # Ganti dengan nama file YAML yang diinginkan

with open(file_path, 'w') as file:
    yaml.dump(data, file, default_flow_style=False, sort_keys=False)

print(f"File YAML telah dibuat: {file_path}")