from PIL import Image
import tkinter as tk
from tkinter.filedialog import askopenfilename
import start

def forimagedialog():
    global result
    result.destroy()
    
    global imagename
    imagename=askopenfilename(filetypes=[('Image',['*.JPG','*.BMP','*.PNG'])])
    global imgtxt
    imgtxt.destroy()
    imgtxt=tk.Text(Encryptpanel,height=1,width=500)
    imgtxt.insert(tk.INSERT,'Image:  '+imagename)
    imgtxt.configure(state=tk.DISABLED)
    imgtxt.place(x=0,y=60)
    check()

def fortextdialog():  
    global result
    result.destroy()
    
    global filename
    filename=askopenfilename(filetypes=[('Text File',['*.txt'])])
    global filetxt
    filetxt.destroy()
    filetxt=tk.Text(Encryptpanel,height=1,width=500)
    filetxt.insert(tk.INSERT,'TextFile:  '+filename)
    filetxt.configure(state=tk.DISABLED)
    filetxt.place(x=0,y=85)
    check()

def decryptimage():
    global result
    result.destroy()
    
    global decimage
    decimage=askopenfilename(filetypes=[("Image File",["*.jpg","*.bmp","*.png"])])
    global decryptbut
    decryptbut.destroy()
    global decimgtxt
    decimgtxt.destroy()
    decimgtxt=tk.Text(Encryptpanel,height=1,width=500)
    decimgtxt.insert(tk.INSERT,'Decrypt Image : '+decimage)
    decimgtxt.configure(state=tk.DISABLED)
    decimgtxt.place(x=0,y=70)
    
    if(decimage!=''):
        decryptbut=tk.Button(Encryptpanel,text="Decrypt",font=("Trebuchet MS bold",12),fg='white',command=startdecryption)
        decryptbut.configure(background='#1E88E5')
        decryptbut.place(x=320,y=110)
        

def check():
    global result
    result.destroy()
    global Next
    Next.destroy()
    if(filename!='' and imagename!=''):
        Next=tk.Button(Encryptpanel,text="Encrypt",font=("Trebuchet MS bold",12),fg='white',command=startencryption)
        Next.configure(background='#1E88E5')
        Next.place(x=320,y=120)

def startencryption():
    global filename
    global imagename
    global result
    
    result.destroy()
    t=start.startencryption(imagename,filename)
    result=tk.Label(Encryptpanel,text=t)
    result.place(x=275,y=180)
    

def startdecryption():
    global decimage
    global result
    
    result.destroy()
    t=start.startdecryption(decimage)
    result=tk.Label(Encryptpanel,text=t)
    result.place(x=275,y=180)

def encrypttab():
    getimage.destroy()
    decimgtxt.destroy()
    decryptbut.destroy()
    result.destroy()
    
    global selectimage
    selectimage=tk.Button(Encryptpanel,text="Select Image",font=("Trebuchet MS bold",12),fg='white',command=forimagedialog)
    selectimage.configure(background='#1E88E5')
    selectimage.place(x=200,y=0)
    
    global selecttextfile
    selecttextfile=tk.Button(Encryptpanel,text="Select File",font=("Trebuchet MS bold",12),fg='white',command=fortextdialog)
    selecttextfile.configure(background='#1E88E5')
    selecttextfile.place(x=400,y=0)

def decrypttab():
    selectimage.destroy()
    global filename
    filename=''
    global imagename
    imagename=''
    selecttextfile.destroy()
    imgtxt.destroy()
    filetxt.destroy()
    Next.destroy()
    result.destroy()
    
    global getimage
    getimage=tk.Button(Encryptpanel,text="Select Image",font=("Trebuchet MS bold",12),fg='white',command=decryptimage)
    getimage.configure(background='#1E88E5')
    getimage.place(x=300,y=0)

filename=''
imagename=''
decimage=''

window=tk.Tk()
window.geometry('700x400')
window.title("LSB Stegnography")
window.configure(background='#ffffff')
                 
Subject=tk.Label(window,text="Select for\n Stegnogrpahy:",font=("Trebuchet MS",20),fg="#1e88e5")
Subject.place(x=250,y=60)
Subject.configure(background='white')

encrypt=tk.Radiobutton(window,text="Encrypt",font=("Trebuchet MS bold",12),command=encrypttab)
encrypt.configure(background='white')
encrypt.place(x=250,y=150)

decrypt=tk.Radiobutton(window,text="Decrypt",font=("Trebuchet MS bold",12),command=decrypttab)
decrypt.configure(background='white')
decrypt.place(x=360,y=150)

Encryptpanel=tk.PanedWindow(width=700,height=200,background='white')

selectimage=tk.Button()
selecttextfile=tk.Button()
getimage=tk.Button()
filetxt=tk.Text()
imgtxt=tk.Text()
decimgtxt=tk.Text()
Next=tk.Button()
decryptbut=tk.Button()
result=tk.Label()

Encryptpanel.place(x=0,y=190)

window.mainloop()
