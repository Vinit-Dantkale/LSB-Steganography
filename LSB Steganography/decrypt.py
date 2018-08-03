import numpy as np
from PIL import Image

def openimage(imagefile):
    #Open the image 
    igs=Image.open(imagefile)
    imgs=np.asarray(igs,dtype=np.uint8)
    return imgs


def decrypt(imgs):
    #Till (000000) Null of ASCII is not found keep searching
    #Once found break
    bintext=''
    letter=''
    for row in imgs:
        for pixels in row:
            letter=letter+'{0:08b}'.format(pixels[0])[-2:]
            if(len(letter)>=8):
                if(letter[-8:]=='00000000'):
                    break
                bintext=bintext+chr(int(letter,2))
                letter=''
            letter=letter+'{0:08b}'.format(pixels[1])[-2:]
            if(len(letter)>=8):
                if(letter[-8:]=='00000000'):
                    break
                bintext=bintext+chr(int(letter,2))
                letter=''
            letter=letter+'{0:08b}'.format(pixels[2])[-2:]
            if(len(letter)>=8):
                if(letter[-8:]=='00000000'):
                    break
                bintext=bintext+chr(int(letter,2))
                letter=''
    #print(bintext)
    t=open("NewTextFile.txt",'w')
    t.write(bintext)