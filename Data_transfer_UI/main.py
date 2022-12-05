from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys
import os
import shutil
import fnmatch
import natsort
import time

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load UI file
        uic.loadUi("main.ui", self)


        ''' Defining Widget '''
        # Buttons
        self.rgb_source_button = self.findChild(QPushButton, "pushButton_5")
        self.rgb_staging_button = self.findChild(QPushButton, "pushButton_6")
        self.rgb_destination_button = self.findChild(QPushButton, "pushButton_4")

        self.thz_source_button = self.findChild(QPushButton, "pushButton")
        self.thz_staging_button = self.findChild(QPushButton, "pushButton_2")
        self.thz_destination_button = self.findChild(QPushButton, "pushButton_3")

        self.stage_button = self.findChild(QPushButton, "pushButton_7")
        self.commit_button = self.findChild(QPushButton, "pushButton_8")

        self.next_button = self.findChild(QPushButton, "pushButton_10")
        self.previous_button = self.findChild(QPushButton, "pushButton_9")
        self.clear_stage_button = self.findChild(QPushButton, "pushButton_11")

        # Labels
        self.rgb_source_label = self.findChild(QLabel, "label_10")
        self.rgb_staging_label = self.findChild(QLabel, "label_13")
        self.rgb_destination_label = self.findChild(QLabel, "label_15")

        self.thz_source_label = self.findChild(QLabel, "label_7")
        self.thz_staging_label = self.findChild(QLabel, "label_8")
        self.thz_destination_label = self.findChild(QLabel, "label_9")

        self.rgb_image = self.findChild(QLabel, "label")
        self.thz_image = self.findChild(QLabel, "label_2")

        self.rgb_image_label = self.findChild(QLabel, "label_3")
        self.thz_image_label = self.findChild(QLabel, "label_16")
        
        self.rgb_count_label = self.findChild(QLabel, "label_21")
        self.thz_count_label = self.findChild(QLabel, "label_22")

        self.status_label = self.findChild(QLabel, "label_17")
        self.clear_stage_label = self.findChild(QLabel, "label_23")


        # Set default directory
        self.rgb_source_directory = "C:/Users/CHB3SGP/Desktop/test_directory/rgb_source"
        self.rgb_staging_directory = "C:/Users/CHB3SGP/Desktop/test_directory/rgb_staging"
        self.rgb_destination_directory = "C:/Users/CHB3SGP/Desktop/test_directory/rgb_destination"

        self.thz_source_directory = "C:/Users/CHB3SGP/Desktop/test_directory/thz_source"
        self.thz_staging_directory = "C:/Users/CHB3SGP/Desktop/test_directory/thz_staging"
        self.thz_destination_directory = "C:/Users/CHB3SGP/Desktop/test_directory/thz_destination"

        self.rgb_source_label.setText(self.rgb_source_directory)
        self.rgb_staging_label.setText(self.rgb_staging_directory)
        self.rgb_destination_label.setText(self.rgb_destination_directory)

        self.thz_source_label.setText(self.thz_source_directory)
        self.thz_staging_label.setText(self.thz_staging_directory)
        self.thz_destination_label.setText(self.thz_destination_directory)


        ''' Button Functions '''
        # Choose directory button
        self.rgb_source_button.clicked.connect(lambda: self.choose_directory(1))
        self.rgb_staging_button.clicked.connect(lambda: self.choose_directory(2))
        self.rgb_destination_button.clicked.connect(lambda: self.choose_directory(3))

        self.thz_source_button.clicked.connect(lambda: self.choose_directory(4))
        self.thz_staging_button.clicked.connect(lambda: self.choose_directory(5))
        self.thz_destination_button.clicked.connect(lambda: self.choose_directory(6))

        self.stage_button.clicked.connect(self.stage)

        self.next_button.clicked.connect(self.next)
        self.previous_button.clicked.connect(self.previous)
        self.commit_button.clicked.connect(self.commit)
        self.clear_stage_button.clicked.connect(self.clear_stage)

        ''' Default Button Status '''
        if not (self.rgb_source_directory and self.rgb_staging_directory and self.rgb_destination_directory and self.thz_source_directory and self.thz_staging_directory and self.thz_destination_directory):
            self.stage_button.setEnabled(False)
        
        self.next_button.setEnabled(False)
        self.previous_button.setEnabled(False)
        self.commit_button.setEnabled(False)

        # Show app
        self.show()


    def choose_directory(self, label_num):
        # Open file dialog
        directory = QFileDialog.getExistingDirectory(self, "Select Folder")
    
        # Output filename to screen
        if directory and label_num == 1:
            self.rgb_source_directory = directory
            self.rgb_source_label.setText(self.rgb_source_directory)
            if (self.rgb_source_directory and self.rgb_staging_directory and self.rgb_destination_directory and self.thz_source_directory and self.thz_staging_directory and self.thz_destination_directory):
                self.stage_button.setEnabled(True)
        
        if directory and label_num == 2:
            self.rgb_staging_directory = directory
            self.rgb_staging_label.setText(self.rgb_staging_directory)
            if (self.rgb_source_directory and self.rgb_staging_directory and self.rgb_destination_directory and self.thz_source_directory and self.thz_staging_directory and self.thz_destination_directory):
                self.stage_button.setEnabled(True)
    
        if directory and label_num == 3:
            self.rgb_destination_directory = directory
            self.rgb_destination_label.setText(self.rgb_destination_directory)
            if (self.rgb_source_directory and self.rgb_staging_directory and self.rgb_destination_directory and self.thz_source_directory and self.thz_staging_directory and self.thz_destination_directory):
                self.stage_button.setEnabled(True)

        if directory and label_num == 4:
            self.thz_source_directory = directory
            self.thz_source_label.setText(self.thz_source_directory)
            if (self.rgb_source_directory and self.rgb_staging_directory and self.rgb_destination_directory and self.thz_source_directory and self.thz_staging_directory and self.thz_destination_directory):
                self.stage_button.setEnabled(True)
       
        if directory and label_num == 5:
            self.thz_staging_directory = directory
            self.thz_staging_label.setText(self.thz_staging_directory)
            if (self.rgb_source_directory and self.rgb_staging_directory and self.rgb_destination_directory and self.thz_source_directory and self.thz_staging_directory and self.thz_destination_directory):
                self.stage_button.setEnabled(True)
         
        if directory and label_num == 6:
            self.thz_destination_directory = directory
            self.thz_destination_label.setText(self.thz_destination_directory)
            if (self.rgb_source_directory and self.rgb_staging_directory and self.rgb_destination_directory and self.thz_source_directory and self.thz_staging_directory and self.thz_destination_directory):
                self.stage_button.setEnabled(True)
           

    def stage(self):
        global rgb_cardboard_count
        global rgb_pet_count
        global rgb_hdpe_count

        global thz_cardboard_count
        global thz_pet_count
        global thz_hdpe_count
        
        rgb_cardboard_count = 0
        rgb_pet_count = 0
        rgb_hdpe_count = 0

        thz_cardboard_count = 0
        thz_pet_count = 0
        thz_hdpe_count = 0

        for rgb_image in os.listdir(self.rgb_destination_directory):

            if fnmatch.fnmatch(rgb_image, "Cardboard*"):
                rgb_cardboard_count += 1
            
            if fnmatch.fnmatch(rgb_image, "PET*"):
                rgb_pet_count += 1

            if fnmatch.fnmatch(rgb_image, "HDPE*"):
                rgb_hdpe_count += 1
        
        for thz_image in os.listdir(self.thz_destination_directory):

            if fnmatch.fnmatch(thz_image, "Cardboard*"):
                thz_cardboard_count += 1
            
            if fnmatch.fnmatch(thz_image, "PET*"):
                thz_pet_count += 1

            if fnmatch.fnmatch(thz_image, "HDPE*"):
                thz_hdpe_count += 1
        
        # print(f"RGB Count: {rgb_cardboard_count}")
        # print(f"THZ Count: {thz_cardboard_count}")

        for rgb_source_image in os.listdir(self.rgb_source_directory):
            
            if fnmatch.fnmatch(rgb_source_image, "Cardboard*"):
                shutil.copy(os.path.join(self.rgb_source_directory, rgb_source_image), os.path.join(self.rgb_staging_directory, f"Cardboard_RGB_{rgb_cardboard_count}.jpg"))
                rgb_cardboard_count += 1
            
            if fnmatch.fnmatch(rgb_source_image, "PET*"):
                shutil.copy(os.path.join(self.rgb_source_directory, rgb_source_image), os.path.join(self.rgb_staging_directory, f"PET_RGB_{rgb_pet_count}.jpg"))
                rgb_pet_count += 1
            
            if fnmatch.fnmatch(rgb_source_image, "HDPE*"):
                shutil.copy(os.path.join(self.rgb_source_directory, rgb_source_image), os.path.join(self.rgb_staging_directory, f"HDPE_RGB_{rgb_hdpe_count}.jpg"))
                rgb_hdpe_count += 1

        for thz_source_image in os.listdir(self.thz_source_directory):
            
            if fnmatch.fnmatch(thz_source_image, "Cardboard*"):
                shutil.copy(os.path.join(self.thz_source_directory, thz_source_image), os.path.join(self.thz_staging_directory, f"Cardboard_THZ_{thz_cardboard_count}.jpg"))
                thz_cardboard_count += 1
            
            if fnmatch.fnmatch(thz_source_image, "PET*"):
                shutil.copy(os.path.join(self.thz_source_directory, thz_source_image), os.path.join(self.thz_staging_directory, f"PET_THZ_{thz_pet_count}.jpg"))
                thz_pet_count += 1
            
            if fnmatch.fnmatch(thz_source_image, "HDPE*"):
                shutil.copy(os.path.join(self.thz_source_directory, thz_source_image), os.path.join(self.thz_staging_directory, f"HDPE_THZ_{thz_hdpe_count}.jpg"))
                thz_hdpe_count += 1

        self.commit_button.setEnabled(True)
        self.next_button.setEnabled(True)
        self.previous_button.setEnabled(True)

        self.clear_stage_label.setText("")
        self.status_label.setText("")

        global rgb_staging_image
        global thz_staging_image

        self.rgb_image_index = 0
        self.thz_image_index = 0

        rgb_staging_image = natsort.natsorted(os.listdir(self.rgb_staging_directory))
        thz_staging_image = natsort.natsorted(os.listdir(self.thz_staging_directory))

        self.display_rgb_image()
        self.display_thz_image()


    def display_rgb_image(self):
        # Resize dimensions
        w = 465
        h = 369

        self.pixmap_1 = QPixmap(os.path.join(self.rgb_staging_directory, rgb_staging_image[self.rgb_image_index]))
        self.rgb_image.setPixmap(self.pixmap_1.scaled(w, h, QtCore.Qt.KeepAspectRatio))
        self.rgb_image_label.setText(rgb_staging_image[self.rgb_image_index])
        self.rgb_count_label.setText(f"{self.rgb_image_index + 1} of {len(os.listdir(self.rgb_staging_directory))}")

    def display_thz_image(self):
        # Resize dimensions
        w = 465
        h = 369

        self.pixmap_2 = QPixmap(os.path.join(self.thz_staging_directory, thz_staging_image[self.thz_image_index]))
        self.thz_image.setPixmap(self.pixmap_2.scaled(w, h, QtCore.Qt.KeepAspectRatio))
        self.thz_image_label.setText(thz_staging_image[self.thz_image_index])
        self.thz_count_label.setText(f"{self.thz_image_index + 1} of {len(os.listdir(self.thz_staging_directory))}")


    def next(self):
        if self.rgb_image_index + 1 < len(os.listdir(self.rgb_staging_directory)):
            self.rgb_image_index += 1

        if self.thz_image_index + 1 < len(os.listdir(self.thz_staging_directory)):
            self.thz_image_index += 1

        try: 
            self.display_rgb_image()
        except: 
            pass
        try:
            self.display_thz_image()
        except:
            pass


    def previous(self):
        if self.rgb_image_index > 0:
            self.rgb_image_index -= 1
        
        if self.thz_image_index > 0:
            self.thz_image_index -= 1
        try: 
            self.display_rgb_image()
        except: 
            pass
        try:
            self.display_thz_image()
        except:
            pass
    
    def commit(self):
        for rgb_image in os.listdir(self.rgb_staging_directory):
            shutil.move(os.path.join(self.rgb_staging_directory, rgb_image), self.rgb_destination_directory)
        
        for thz_image in os.listdir(self.thz_staging_directory):
            shutil.move(os.path.join(self.thz_staging_directory, thz_image), self.thz_destination_directory)
        
        self.commit_button.setEnabled(False)
        self.status_label.setText("Commit Complete")
        self.next_button.setEnabled(False)
        self.previous_button.setEnabled(False)
    
    def clear_stage(self):
        try: 
            for rgb_files in os.listdir(self.rgb_staging_directory):
                os.remove(os.path.join(self.rgb_staging_directory, rgb_files))
            
            for thz_files in os.listdir(self.thz_staging_directory):
                os.remove(os.path.join(self.thz_staging_directory, thz_files))
            
            self.clear_stage_label.setText("Staging Cleared")
            
        except:
            pass
        
        
# Initialize app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()