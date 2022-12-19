import cv2 as cv
import os

def frame_extract(DIR, FPS):
    fps = 0
    check = FPS
    for i in os.listdir(DIR):

        count = 1
        save_path = os.path.join(DIR, i[:-4])
        os.mkdir(save_path)
        path = os.path.join(DIR, i)
        video = cv.VideoCapture(path)
            
        if check == None:

            if "RGB" in i:
                FPS = 2
            elif "THZ" in i: 
                FPS = 1
        
        print(f"FPS: {FPS}")

        while video.isOpened():
            ret, frame = video.read()

            if ret:
                cv.imwrite(os.path.join(save_path, f'{i[:-4]}_{count}.jpg'), frame)
                add_frame = 30/FPS
                fps += int(add_frame)
                video.set(cv.CAP_PROP_POS_FRAMES, fps)
                print(f"Extracting frame: {count}")
                count += 1

            else:
                video.release()
                break
    print("Extraction complete!")


if __name__ == "__main__":

    '''
    1. Ensure that the videos are named as example: 10-Jan-22_RGB_PET_Clean.avi or 10-Jan-22_THZ_Cardboard.avi.
    3. Change DIR to the path containing the videos.
    4. Frames will be extracted and saved in DIR.
    '''

    # Directory containing all raw videos
    DIR = r"C:\Users\CHB3SGP\Desktop\Lab_Data"

    # No. of frames to extract per second. (RGB = 2) (THZ = 1)
    # Default is 'None'. Unless you want to specify FPS to extract
    FPS = None

    frame_extract(DIR, FPS)


