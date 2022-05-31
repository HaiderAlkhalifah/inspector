import os
import cv2
import shutil
import face_recognition

def main():
    path1 = input("Enter the location of the image: ")
    path2 = input("Enter the location of the folder: ")
    new_dir_name = input("Name the new folder: ")
    new_dir_path = input("Enter the location of the new folder: ")
    
    new_folder_path = dir_mkr(new_dir_path,new_dir_name)

    file_path = ls_imgs_mkr(path2)

    for images in range(len(file_path)):

        result = face_reco(path1,str(file_path[images]))

        if result == [True]:

            shutil.copy2(str(file_path[images]),new_folder_path)

def dir_mkr(path,dire_name):
    
    try:
        compete_path = os.path.join(path,dire_name)
        os.mkdir(compete_path)
        return compete_path
        
    except OSError as error:

        print(f"Error: {error}")

def ls_imgs_mkr(path):

    ls_imgs_names = os.listdir(path)
    ls_imgs_path = [os.path.join(path, img) for img in ls_imgs_names]
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
