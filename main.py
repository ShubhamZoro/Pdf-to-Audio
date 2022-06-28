import PyPDF2
import pyttsx3
import pdfplumber
from tkinter import *
from tkinter.ttk import *
engine = pyttsx3.init()
def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()
# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.title("Pdf file")
root.geometry('200x100')


# This function will be used to open
# file in read mode and only pdf files
# will be opened
def open_file():
    file = askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file is not None:
        text = file.read()
        fun_talk(text)


btn = Button(root, text='Open', command=lambda:open_file())
btn.pack(side=TOP, pady=25,padx=50)

mainloop()

