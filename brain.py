import os
import cv2
import face_recognition

def main():
    path1 = input("Enter the location of the image: ")
    path2 = input("Enter the location of the folder: ") 

    file_path = ls_Imgs_Mkr(path2)

    for images in range(len(file_path)):
        face_reco(path1,str(file_path[images]))


def ls_Imgs_Mkr(path):

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

    #result = face_recognition.compare_faces([knownFace_encoding], unknown_encoding)

    for _ , each_face_encoding in zip(unknown_location, unknown_encoding):
        
        result = face_recognition.compare_faces([knownFace_encoding],each_face_encoding)
        
        if result == [True]:

            return print(result)
        
    
main()
