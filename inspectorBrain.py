import os
import face_recognition

def main():
    path1 = input("Enter the location of the image: ")
    path2 = input("Enter the location of the folder: ") 

    filePath = lsImgsMkr(path2)

    for images in range(len(filePath)):
        faceReco(path1,str(filePath[images]))


def lsImgsMkr(path):

    ls_imgs_names = os.listdir(path)
    ls_imgs_path = [os.path.join(path, img) for img in ls_imgs_names]
    return ls_imgs_path


def faceReco(known,unknown):

    known_image = face_recognition.load_image_file(known)
    unknown_image = face_recognition.load_image_file(unknown)

    knownFace_encoding = face_recognition.face_encodings(known_image)[0]
    knownFace_locoding = face_recognition.face_locations(known_image)[0]

    unknown_encoding = face_recognition.face_encodings(unknown_image)[0] 
    unknown_locoding = face_recognition.face_locations(unknown_image)[0] 

    result = face_recognition.compare_faces([knownFace_encoding], unknown_encoding)

    return print(result)
    
    
main()
