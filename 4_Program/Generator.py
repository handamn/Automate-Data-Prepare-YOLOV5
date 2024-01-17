import os
import random
import shutil
import yaml
import subprocess

import os

# Clear screen command
os.system('cls' if os.name == 'nt' else 'clear')


BASIS_FOLDER = "/home/pcsistem/camera_vision_develop/"

def run_python_file(file_name, arguments=None):
    try:
        subprocess.run(["python", file_name] + (arguments or []), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def data_input_default():
    car           = input("Enter Car Model           (ex : Innova)          : ")
    steer         = input("Enter Steer               (ex : RHD)             : ")
    box           = input("Enter Box Class           (ex : Box1)            : ")
    kode_box      = input("Enter Code Box            (ex : X_3_CDE)         : ")
    kendaraan = car + "_" + steer

    return kendaraan, box, kode_box

def data_input():
    epochs_count  = input("Enter How Many Epochs     (ex : 100)             : ")
    model_type    = input("Enter Train Model Conf    (ex : yolov5l_CBAM_2)  : ")
    batch_count   = input("Enter Batch Count         (ex : -1)              : ")
    pat_count     = input("Enter Patience            (ex : 100)             : ")

    return epochs_count, model_type, batch_count, pat_count

def activate_label(confirm):
    konfirmasi = confirm
    home_folder = f'cd {BASIS_FOLDER}'
    activate_script = f'source Z_LabelImg/bin/activate'

    if konfirmasi == "Yes":
        print("\n\n")
    else:
        print(f"\n{home_folder}\n{activate_script}\ncd 4_Program\n")

def activate_conda(confirm):
    if confirm == "Yes":
        print("\n")
    else:
        print("conda activate Engser1")



def copy_random_images(source_folder, destination_folder, num_images):
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    num_images = min(num_images, len(image_files))
    random_images = random.sample(image_files, num_images)

    for image in random_images:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        shutil.copy2(source_path, destination_path)
        print(f"Copied: {image}")

def print_menu():
    print("\nProgram Generator\n")
    print("Pilih Menu :")
    print("1. Ambil Gambar")
    print("2. Pilih Random 50")
    print("3. Anotasi")
    print("4. Training Prepare Image")
    print("5. Auto Anotasi")
    print("6. Combine")
    print("7. Training Final\n")

    hasil_menu    = input("Enter Menu                                       : ")
    # Clear screen command
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================================")

    return hasil_menu

pilih_menu = print_menu()

if pilih_menu == "1":
    nama_file_lain = f"{BASIS_FOLDER}4_Program/trial_ambil_gambar_v1.py"
    run_python_file(nama_file_lain)

elif pilih_menu == "2":
    out_or_in     = input("Enter Production Line     (ex : Out_line)        : ")
    kendaraan, box, kode_box = data_input_default()
    jumlah_gambar = input("Enter How Many Image      (ex : 100)             : ")

    source_folder = f'{BASIS_FOLDER}2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/images/'
    automasi_folder = f'{BASIS_FOLDER}2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/X_Automasi/'
    sub_automasi_images_folder = os.path.join(automasi_folder, 'images')
    sub_automasi_labels_folder = os.path.join(automasi_folder, 'labels')

    for folder in [automasi_folder, sub_automasi_images_folder, sub_automasi_labels_folder]:
        os.makedirs(folder, exist_ok=True)

    value_data = kode_box
    file_path_2 = f'{sub_automasi_labels_folder}/classes.txt'

    with open(file_path_2, 'w') as file:
        file.write(value_data)

    destination_folder = sub_automasi_images_folder
    copy_random_images(source_folder, destination_folder, int(jumlah_gambar))

    data = {
        'train': automasi_folder,
        'val': automasi_folder,
        'names': {0: kode_box}
    }

    file_path = f'{automasi_folder}{kode_box}.yaml'  
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

    print(f"File TXT telah dibuat: {file_path_2}")
    print(f"File YAML telah dibuat: {file_path}")

elif pilih_menu == "3":
    program = "labelImg"
    konfirmasi2   = input("Is the Label active?      (ex : Yes / No)        : ")
    out_or_in     = input("Enter Production Line     (ex : Out_line)        : ")
    kendaraan, box, kode_box = data_input_default()
    root_folder = f'{BASIS_FOLDER}2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/X_Automasi'

    folder_image = f'{root_folder}/images'
    folder_label = f'{root_folder}/labels/classes.txt'
    string_script = f'{program} {folder_image} {folder_label}'

    print("\nCopy dari Bawah Border Ini\n======================================================\n")
    activate_label(konfirmasi2)
    print(string_script)
    print("deactivate\n")
    print("======================================================\nSampai Sebelum Border Ini\n")

elif pilih_menu == "4":
    out_or_in     = input("Enter Production Line     (ex : Out_line)        : ")
    kendaraan, box, kode_box = data_input_default()
    epochs_count, model_type, batch_count, pat_count = data_input()

    #DATA
    data_source = f'{BASIS_FOLDER}2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/X_Automasi/{kode_box}.yaml'
    
    #PROJECT
    project_source = f'{BASIS_FOLDER}2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/Models'

    #EPOCH
    epochs_source = epochs_count

    #CFG
    cfg_source = f'{BASIS_FOLDER}4_Program/yolov5/models/{model_type}.yaml'

    #BATCH-SIZE
    batch_size_source = batch_count

    #PATIENCE
    patience_size_source = pat_count

    #PERINTAH TRAIN
    nama_file_lain = f'{BASIS_FOLDER}4_Program/yolov5/train.py'
    argumen = ["--data", f"{data_source}",
            "--project", f"{project_source}",
            "--epochs", f"{epochs_source}", 
            "--weights", "", 
            "--cfg", f"{cfg_source}",
            "--batch-size", f"{batch_size_source}", 
            "--patience", f"{patience_size_source}"]

    #SCRIPT TOTAL
    run_python_file(nama_file_lain, argumen)
    print("\n======================================================")
    print(f"Proses Training Modal ={kendaraan}-{box}-{kode_box}=")
    print("======================BERHASIL=======================\n")

elif pilih_menu == "5":
    nama_file_lain = f"{BASIS_FOLDER}4_Program/yolov5/trial_auto_anotasi_v4.py"
    run_python_file(nama_file_lain)

elif pilih_menu == "6":
    nama_file_lain = f"{BASIS_FOLDER}4_Program/trial_combine_v9.py"
    run_python_file(nama_file_lain)

elif pilih_menu == "7":
    kendaraan, box, kode_box = data_input_default()
    epochs_count, model_type, batch_count, pat_count = data_input()

    #DATA
    data_source = f'{BASIS_FOLDER}5_STUDIO_MAKER/{kendaraan}/{box}/{kode_box}/{kode_box}.yaml'

    #PROJECT
    project_source = f'{BASIS_FOLDER}5_STUDIO_MAKER/{kendaraan}/{box}/{kode_box}/Models'

    #EPOCH
    epochs_source = epochs_count

    #CFG
    cfg_source = f'{BASIS_FOLDER}4_Program/yolov5/models/{model_type}.yaml'

    #BATCH-SIZE
    batch_size_source = batch_count

    #PATIENCE
    patience_size_source = pat_count

    #PERINTAH TRAIN
    nama_file_lain = f'{BASIS_FOLDER}4_Program/yolov5/train.py'
    argumen = ["--data", f"{data_source}",
            "--project", f"{project_source}",
            "--epochs", f"{epochs_source}", 
            "--weights", "", 
            "--cfg", f"{cfg_source}",
            "--batch-size", f"{batch_size_source}", 
            "--patience", f"{patience_size_source}"]

    #SCRIPT TOTAL
    run_python_file(nama_file_lain, argumen)
    print("\n======================================================")
    print(f"Proses Training Final ={kendaraan}-{box}-{kode_box}=")
    print("======================BERHASIL=======================\n")
