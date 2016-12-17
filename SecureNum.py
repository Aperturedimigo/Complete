import os

def chkNumbers(num):
    if open('number.txt', 'r').readline() == str(num):
        return True
    else:
        return False

def saveNumbers(num):
    with open('number.txt', 'w') as f:
        f.write(num)
        f.close()

def removeNumbers():
    os.remove('number.txt')
