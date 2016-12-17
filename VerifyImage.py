import Minsung.Face_list as fl
import Minsung.Face as f

face_list_id = open('name.txt', 'r').readline()

def getSecondImage(face_list_id, image):
    data = yaml.load(fl.add_face(image,face_list_id))
    with open('ps2.txt', 'w') as f:
        f.write(data)
        f.close()

def compare():
    if open('ps1.txt', 'r').readline() == open('ps2.txt', 'r').readline():
        
