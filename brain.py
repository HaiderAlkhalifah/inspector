import os
import cv2
import shutil
import face_recognition
from tkinter import filedialog
from tkinter import *

def main():
    path1 = image_picker()
    path2 = dir_root()
    #new_dir_name = input("Name the new folder: ")
    new_dir_path = new_folder_root()
    
    new_folder_path = dir_mkr(new_dir_path)

    file_path = ls_imgs_mkr(path2)

    for images in range(len(file_path)):

        result = face_reco(path1,str(file_path[images]))

        if result == [True]:

            shutil.copy2(str(file_path[images]),new_folder_path)

def image_picker():
    root = Tk()
    root.filename =  filedialog.askopenfilename(
        initialdir = "/",title = "Select the image",filetypes = (("jpeg files","*.jpg"),("png files","*.png*"))
        )
    return root.filename

def new_folder_root():
    root = Tk()
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file")
    return root.filename

def dir_root():
    file = filedialog.askdirectory()
    return file

def dir_mkr(path):
    
    try:
        compete_path = os.path.join(path)
        os.mkdir(compete_path)
        return compete_path
        
    except OSError as error:

        print(f"Error: {error}")

def ls_imgs_mkr(path):

    ls_imgs_names = os.listdir(str(path))
    ls_imgs_path = [os.path.join(str(path), img) for img in ls_imgs_names]
    return ls_imgs_path


def face_reco(known,unknown):

    known_image = face_recognition.load_image_file(known)
    known_image = cv2.cvtColor(known_image, cv2.COLOR_BGR2RGB)
    knownFace_encoding = face_recognition.face_encodings(known_image)[0]
    knownFace_location = face_recognition.face_locations(known_image)[0]
    
    unknown_image = face_recognition.load_image_file(unknown)
    unknown_image = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
    unknown_encoding = face_recognition.face_encodings(unknown_image) 
    unknown_location = face_recognition.face_locations(unknown_image) 

    for _ , each_face_encoding in zip(unknown_location, unknown_encoding):
        
        result = face_recognition.compare_faces([knownFace_encoding],each_face_encoding)
        
        if result == [True]:

            return result
        
    
main()
