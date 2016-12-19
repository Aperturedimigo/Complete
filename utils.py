import Minsung.Face_list as fl
import Minsung.Face as fa
import yaml, os


#Initial Settings

def setName(name):
    name = name.lower()
    with open('name.txt', 'w') as f:
        f.write(name)
        f.close()

def createMainImage(face_list_id, image):
    fl.create(face_list_id)
    data = yaml.load(fl.add_face(image, face_list_id))['persistedFaceId']
    print(data)

    with open('ps1.txt', 'w') as f:
        f.write(data)
        f.close()


#Verify Image
def getSecondImage(face_list_id, image):
    data = yaml.load(fl.add_face(image,face_list_id))['persistedFaceId']
    with open('ps2.txt', 'w') as f:
        f.write(data)
        f.close()

def compare():
    if open('ps1.txt', 'r').readline() == open('ps2.txt', 'r').readline():
        return True

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
    fl.remove(face_list_id)

