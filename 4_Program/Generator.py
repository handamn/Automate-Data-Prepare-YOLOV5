#####################
basis_folder = "/home/pcsistem/camera_vision_develop/"
#####################

def data_input():
    print(" ")
    car           = input("Enter Car Model             (ex : Innova)         : ")
    steer         = input("Enter Steer                 (ex : RHD)            : ")
    box           = input("Enter Box Class             (ex : Box1)           : ")
    kode_box      = input("Enter Code Box              (ex : X_3_CDE)        : ")
    epochs_count  = input("Enter How Many Epochs       (ex : 100)            : ")
    model_type    = input("Enter Train Model Conf      (ex : yolov5l_CBAM_2) : ")
    batch_count   = input("Enter Batch Count           (ex : -1)             : ")
    pat_count     = input("Enter Patience              (ex : 100)            : ")

    kendaraan  = car + "_" + steer

    return kendaraan, box, kode_box, epochs_count, model_type, batch_count, pat_count

def Activate_Label():
    print(" ")

    konfirmasi    = input("Is the Label active?        (ex : Yes / No)      : ")
    home_folder = f'cd {basis_folder}'
    activate_script = f'source Z_LabelImg/bin/activate'
    program = "labelImg"

    if konfirmasi == "Yes" :
        print("")
        print(program)
        print("")
    
    else:
        print("")
        print(home_folder)
        print(activate_script)
        print(program)
        print("")

def Activate_Conda():
    print("")
    konfirmasi    = input("Is the Conda active?        (ex : Yes / No)      : ")

    if konfirmasi == "Yes":
        print("")
        print("Copy dari Bawah Border Ini")
        print("======================================================")
        print("")
    
    else:
        print("")
        print("Copy dari Bawah Border Ini")
        print("======================================================")
        print("")
        print("conda activate Engser1")
        print("")


print("")
print("Program Generator")
print("")

print("Pilih Menu :")
print("1. Ambil Gambar")
print("2. Anotasi")
print("3. Training Prepare Image")
print("4. Training Final")
print("")

pilih_menu = input("Enter Menu                                        : ")
print("======================================================")

if pilih_menu == "1":
    print("coming_soon")

elif pilih_menu == "2":
    Activate_Label()
    print("")
    print("======================================================")
    print("Sampai Sebelum Border Ini")
    print("")

elif pilih_menu == "3":
    kendaraan, box, kode_box, epochs_count, model_type, batch_count, pat_count = data_input()

    print(" ")
    out_or_in     = input("Enter Production Line       (ex : Out_line)       : ")

    #DATA
    data_source = f'{basis_folder}2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/X_Automasi/{kode_box}.yaml'
    
    #PROJECT
    project_source = f'{basis_folder}2_Stock_Foto/{out_or_in}/{kendaraan}/{box}/{kode_box}/Models'

    #EPOCH
    epochs_source = epochs_count

    #CFG
    cfg_source = f'{basis_folder}4_Program/yolov5/models/{model_type}.yaml'

    #BATCH-SIZE
    batch_size_source = batch_count

    #PATIENCE
    patience_size_source = pat_count

    #SCRIPT TOTAL
    print("")
    Activate_Conda()
    script_train = f"python train.py --data {data_source} --project {project_source} --epochs {epochs_source} --weights '' --cfg {cfg_source} --batch-size {batch_size_source} --patience {patience_size_source}"
    print(script_train)
    print("")
    print("======================================================")
    print("Sampai Sebelum Border Ini")
    print("")


elif pilih_menu == "4":
    kendaraan, box, kode_box, epochs_count, model_type, batch_count, pat_count = data_input()
    #DATA
    data_source = f'{basis_folder}5_STUDIO_MAKER/{kendaraan}/{box}/{kode_box}/{kode_box}.yaml'

    #PROJECT
    project_source = f'{basis_folder}5_STUDIO_MAKER/{kendaraan}/{box}/{kode_box}/Models'

    #EPOCH
    epochs_source = epochs_count

    #CFG
    cfg_source = f'{basis_folder}4_Program/yolov5/models/{model_type}.yaml'

    #BATCH-SIZE
    batch_size_source = batch_count

    #PATIENCE
    patience_size_source = pat_count

    #SCRIPT TOTAL
    print("")
    Activate_Conda()
    script_train = f"python train.py --data {data_source} --project {project_source} --epochs {epochs_source} --weights '' --cfg {cfg_source} --batch-size {batch_size_source} --patience {patience_size_source}"
    print(script_train)
    print("")
    print("======================================================")
    print("Sampai Sebelum Border Ini")
    print("")

