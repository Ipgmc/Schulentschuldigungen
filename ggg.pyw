import os
import tkinter
from tkinter import *
import subprocess
root=tkinter.Tk()
root.iconbitmap("entschuldigung.ico")
rw=tkinter.StringVar()
tw=tkinter.Text(root, font=('Calibri', 12), )

text=open("Entschuldigung.txt", "r")
t=text.read()
tw.insert(END, t)
text.close()
def exec():
    var = tw.get("1.0", "end")
    txt = open("Entschuldigung.txt", "w")
    txt.write(var)
    #txt.close()
    print(var)
    #os.popen("sub.bat")
    subprocess.Popen("sub.bat")


tw.pack()
prin=tkinter.Button(root, text="Fertig", command=exec)
prin.pack()
root.mainloop()