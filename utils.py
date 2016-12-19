import Minsung.Face_list as fl
import Minsung.Face as fa
import yaml, os
#import picamera

#Initial Settings

def setName(name):
    name = name.lower()
    with open('name.txt', 'w') as f:
        f.write(name)
        f.close()
    print("이름이 성공적으로 저장되었습니다.")

def capture():
    return False

def createMainImage(image):
    data = fa.detect(image)[0]["faceId"]
    print(data)
    with open('ps1.txt', 'w') as f:
        f.write(data)
        f.close()

#Verify Image
def getSecondImage(image):
    data = fa.detect(image)[0]["faceId"]
    print(data)
    with open('ps2.txt', 'w') as f:
        f.write(data)
        f.close()
def compare():
    face_id = open('ps1.txt', 'r').readline()
    another_face_id = open('ps2.txt', 'r').readline()
    data =fa.verify(face_id, another_face_id)['confidence']
    if data > 0.7:
        print("우와 성공했어요 시발 드디어 오류를 고쳤어요 !!")
        print(data)
    else:
        print("넌 얼굴이 다르다 거부한다.")



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
    os.remove('name.txt')
    print("초기화가 끝났습니다.")

