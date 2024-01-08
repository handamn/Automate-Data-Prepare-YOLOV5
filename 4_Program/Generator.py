print("APAKAH SUDAH DIAKTIVASI?")
pilih = input("Ya / Belum? : ")


"""
############################
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
############################

#DATA
data_source = f'/home/pcsistem/camera_vision_develop/5_STUDIO_MAKER/{kendaraan}/{box}/{kode_box}/{kode_box}.yaml'

#PROJECT
project_source = f'/home/pcsistem/camera_vision_develop/5_STUDIO_MAKER/{kendaraan}/{box}/{kode_box}/Models'

#EPOCH
epochs_source = epochs_count

#CFG
cfg_source = f'/home/pcsistem/camera_vision_develop/4_Program/yolov5/models/{model_type}.yaml'

#BATCH-SIZE
batch_size_source = batch_count

#PATIENCE
patience_size_source = pat_count

#SCRIPT TOTAL
print("")
script_train = f"python train.py --data {data_source} --project {project_source} --epochs {epochs_source} --weights '' --cfg {cfg_source} --batch-size {batch_size_source} --patience {patience_size_source}"
print(script_train)
print("")
"""



#DATA
home_folder = f'cd /home/pcsistem/camera_vision_develop/'

activate_script = f'source Z_LabelImg/bin/activate'

program = "labelImg"


if pilih == "Ya":
    print("")
    print(program)
    print("")

else :
    print("")
    print(home_folder)
    print(activate_script)
    print(program)
    print("")
