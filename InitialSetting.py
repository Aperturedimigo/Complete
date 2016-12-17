import Minsug.Face_list as fl
import yaml

def getName(name):
    name = ''
    with open('name.txt', 'w') as f:
        f.write(name)
        f.close()

def createMainImage(face_list_id, image):
    fl.create(face_list_id)
    data = yaml.load(fl.add_face(image, face_list_id))
    with open('ps1.txt', 'w') as f:
        f.write(data["persistedFaceId"])
        f.close()

