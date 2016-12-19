import Minsung.Face_list as fl
import Minsung.Face as fa
import yaml, os
from ast import literal_eval

#Initial Settings

def setName(name):
    name = name.lower()
    with open('name.txt', 'w') as f:
        f.write(name)
        f.close()

def createMainImage(face_list_id, image):
    fl.create(face_list_id)
    data = yaml.load(fl.add_face(image, face_list_id))['persistedFaceId']

#Verify Image
def getSecondImage(face_list_id, image):
    data = yaml.load(fl.add_face(image,face_list_id))['persistedFaceId']

def compare(image):
    face_list_id = open('name.txt', 'r').readline()
    face_id = fa.detect(image)[0]['faceId']
    print(face_id)
    print(face_list_id)
    print(type(face_id))
    data = fa.find_similars(face_id,face_list_id)
    print(data)


#Secure number setting
def saveNumbers(num):
    with open('number.txt', 'w') as f:
        f.write(num)
        f.close()

def chkNumbers(num):
    if open('number.txt', 'r').readline() == str(num):
        print("올바른 사용자입니다.")
    else:
        print("올바르지 않은 사용자입니다.")

#Delete settings
def deleteDatas():
    os.remove('ps1.txt')
    os.remove('ps2.txt')
    os.remove('number.txt')
    fl.delete(open('name.txt', 'r').readline())
    print("초기화가 끝났습니다.")

