import os
import shutil

def frame_copy(DIR_FRAME, DIR_LABEL):

    for frame in os.listdir(DIR_FRAME):
        for label in os.listdir(DIR_LABEL):

            if frame[:-4] == label[:-4]:

                shutil.copy(os.path.join(DIR_FRAME, frame), DIR_LABEL)
                print(f"Copying {frame}...")


if __name__ == "__main__":

    # Directory of frames
    DIR_FRAME = r"C:\Users\CHB3SGP\Desktop\Lab_Data\14-Oct-22_THZ_Cardboard"

    # Directory of label
    DIR_LABEL = r"C:\Users\CHB3SGP\Desktop\Lab_Data\14-Oct-22_THZ_Cardboard_Label"

    frame_copy(DIR_FRAME, DIR_LABEL)
