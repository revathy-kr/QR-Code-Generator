import tkinter as tk
from tkinter import *
import pyqrcode
from PIL import  ImageTk,Image
from tkinter import messagebox
import png

def CreateWidgets():
    label=Label(text="ENTER TEXT: ",bg="lightblue")
    label.grid(row=0,column=1,padx=5,pady=5)

    root.entry=Entry(width=30,textvariable=qrInput)
    root.entry.grid(row=0,column=2,padx=5,pady=5)

    button=Button(width=10,text="GENERATE",command=QRCodeGenerate)
    button.grid(row=0,column=3,padx=5,pady=5)

    label = Label(text="QR CODE: ", bg="lightblue")
    label.grid(row=1, column=1, padx=5, pady=5)

    root.ImageLabel=Label(root,background="lightblue")
    root.ImageLabel.grid(row=2,column=1,columnspan=3,padx=5,pady=5)


def QRCodeGenerate():
    qrString=qrInput.get()
    if qrString!="":
        qrGenerate=pyqrcode.create(qrString)
        qrCodePath=""
        qrCodeName=qrCodePath+qrString+".png"
        qrGenerate.png(qrCodeName,scale=10)

        image=Image.open(qrCodeName)
        image.resize((400,400),Image.ANTIALIAS)
        image=ImageTk.PhotoImage(image)

        root.ImageLabel.config(image=image)
        root.ImageLabel.photo=image

    else:
        messagebox.showerror("ERROR","ENTER A TEXT")

root=tk.Tk()
root.title("QR GENERATOR")
root.geometry("510x500")
root.resizable(False,False)
root.config(background="lightblue")

qrInput=StringVar()
CreateWidgets()
root.mainloop()