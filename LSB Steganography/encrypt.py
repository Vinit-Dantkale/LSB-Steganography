import numpy as np
from PIL import Image

s=int()
l=int()

def openimage(imagename):
    #opened with uint8 type
    img=Image.open(imagename)
    temp1=np.asarray(img,dtype=np.uint8)
    temp=temp1.tolist()
    return temp

def opentextfile(filename):
    #opened text and converted to binary format
    t=open(filename,'r').read()
    binletters=''
    for x in str(t):
        binletters=binletters+'{0:08b}'.format(ord(x))
    binletters=binletters+'{0:08b}'.format(0)
    return binletters

def check(temp,binletters):
    # Check if text is very big
    s=len(temp)*len(temp[0])*6
    l=len(binletters)
    if(s>=l):
        return True,s,l
    else:
        return False,s,l

def LSBandsave(temp,binletters,s,l):
    # 1.converted a single value of the pixel to binary format
    # 2.changed the last two digits of binary value
    # 3.Converted to integer Again 
    # 4.If i+2==l then final 2 digits got appended and text ended
    # We have to check after end of every pixel as l%2 can be any
    i=0
    for x in temp:
        for y in x:
            y[0]='{0:08b}'.format(int(y[0]))
            y[0]=str(y[0][0:6])+binletters[i:i+2]
            y[0]=int(y[0],2)
            if i+2<l:
                i=i+2
            else:
                break
            y[1]='{0:08b}'.format(int(y[1]))
            y[1]=str(y[1][0:6])+binletters[i:i+2]
            y[1]=int(y[1],2)
            if i+2<l:
                i=i+2
            else:
                break
            y[2]='{0:08b}'.format(int(y[2]))
            y[2]=str(y[2][0:6])+binletters[i:i+2]
            y[2]=int(y[2],2)
            if i+2<l:
                i=i+2
            else:
                break
            
    temp2=np.asarray(temp,dtype=np.uint8)
    
    #only save as .png 
    #.jpg gives error (lossy compression)
    svimg=Image.fromarray(temp2.astype('uint8'))
    svimg.save("NewImage.png")

#module - embedded message in image