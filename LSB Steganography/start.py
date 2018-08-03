import encrypt as en
import decrypt as de

result=''

def startencryption(imagename,filename):    
    #openimage then openfile then check status
    temp=en.openimage(imagename)
    binletters=en.opentextfile(filename)
    status,s,l=en.check(temp,binletters)
    
    #check status
    if(status):
        en.LSBandsave(temp,binletters,s,l)
        result='File Saved as "NewImage.png"'
    else:
        result="Text File Too Big"
    return result    
    
def startdecryption(decimage):
    imgs=de.openimage(decimage)
    try:
        de.decrypt(imgs)
        result='Text file Saved as "NewTextFile.txt"'
    except Exception as ex:
        result='Select proper Image File'
    return result