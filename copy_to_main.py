import os
import shutil
import fnmatch

def image_count(TARGET_DIR):
    global cardboard_count
    global pet_count
    global hdpe_count

    cardboard_count = 0
    pet_count = 0
    hdpe_count = 0

    for files in os.listdir(TARGET_DIR):

        if fnmatch.fnmatch(files, 'Cardboard*'):
            cardboard_count += 1

        if fnmatch.fnmatch(files, 'PET*'):
            pet_count += 1

        if fnmatch.fnmatch(files, 'HDPE*'):
            hdpe_count += 1
        
        
        
        


def cardboard_count(TARGET_DIR):
    global cardboard_count
    cardboard_count = 0

    for files in os.listdir(TARGET_DIR):
        if fnmatch.fnmatch(files, 'Cardboard*'):
            cardboard_count += 1
    

def pet_count(TARGET_DIR):
    global pet_count
    pet_count = 0

    for files in os.listdir(TARGET_DIR):
        if fnmatch.fnmatch(files, 'PET*'):
            pet_count += 1


def hdpe_count(TARGET_DIR):
    global hdpe_count
    hdpe_count = 0

    for files in os.listdir(TARGET_DIR):
        if fnmatch.fnmatch(files, 'HDPE*'):
            hdpe_count += 1


def transfer(SOURCE_DIR, STAGING_DIR):
    global cardboard_count
    global pet_count
    global hdpe_count

    for files in os.listdir(SOURCE_DIR):
        camera_type = files.split('_')[1]
        
        if fnmatch.fnmatch(files, 'Cardboard*'):
            shutil.copy(os.path.join(SOURCE_DIR, files), os.path.join(STAGING_DIR, f"Cardboard_{camera_type}_{cardboard_count}.jpg"))
            cardboard_count += 1
            print("Copying...")

        if fnmatch.fnmatch(files, 'PET*'):
            shutil.copy(os.path.join(SOURCE_DIR, files), os.path.join(STAGING_DIR, f"PET_{camera_type}_{pet_count}"))
            pet_count += 1
            print("Copying...")
        
        if fnmatch.fnmatch(files, 'HDPE*'):
            shutil.copy(os.path.join(SOURCE_DIR, files), os.path.join(STAGING_DIR, f"HDPE_{camera_type}_{hdpe_count}"))
            hdpe_count += 1
            print("Copying...")


def copy_to_target(STAGING_DIR, TARGET_DIR):
    while True:
        user_input = input("Continue copying to target directory? y/n ")
        if user_input == 'y' or 'n':
            break
        else:
            print("Input is unrecognisable")

    if user_input == 'y':
            for files in os.listdir(STAGING_DIR):
                shutil.move(os.path.join(STAGING_DIR, files), TARGET_DIR)
    
    if user_input == 'n':
        print("Failed to copy")



if __name__ == "__main__":

    SOURCE_DIR = r"C:/Users/CHB3SGP/Desktop/Cardboard/Main_RGB"
    TARGET_DIR = r"C:/Users/CHB3SGP/Desktop/Main_RGB"
    STAGING_DIR = r"C:/Users/CHB3SGP/Desktop/Staging"

    cardboard_count(TARGET_DIR)
    pet_count(TARGET_DIR)
    hdpe_count(TARGET_DIR)
    
    transfer(SOURCE_DIR, STAGING_DIR)
    copy_to_target(STAGING_DIR, TARGET_DIR)



