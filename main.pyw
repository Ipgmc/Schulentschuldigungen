import tkinter
import subprocess
import os
def exec():

    if vv.get()==1:
        text="Sehr geehrter Herr " + tv.get() + "," + "\n\n"
        if v.get() == 1:
            text = text + "Hiermit möchte ich meinen Sohn " + cname.get() + " vom Unterricht für den " + ttv.get() + " freistellen."
        else:
            text = text + "Hiermit möchte ich meine Tochter "+ cname.get() + " vom Unterricht für den " + ttv.get() + " freistellen."
    else:
        text="Sehr geehrte Frau " + tv.get() + "," + "\n\n"
        if v.get() == 1:
            text = text + "Hiermit möchte ich meinen Sohn " + cname.get() + " vom Unterricht für den " + ttv.get() + " freistellen."
        else:
            text = text + "Hiermit möchte ich meine Tochter "+ cname.get() + " vom Unterricht für den " + ttv.get() + " freistellen."
    text=text+"\n\n"+"Mit freundlichem Gruß\n\n"+tvvv.get()
    file=open("Entschuldigung.txt", "w")
    file.write(text)
    os.popen("ggg.exe")
root=tkinter.Tk()
root.iconbitmap("entschuldigung.ico")

root.geometry("500x350")
root.title("Entschuldigungen")
title=tkinter.Label(root, text="Anrede:")
title.grid(row=2, column=2)
vv = tkinter.IntVar()
tkinter.Radiobutton(root, text='Herr',width =25, variable=vv, value=1).grid(row=3, column=3)
tkinter.Radiobutton(root, text='Frau',width =25, variable=vv, value=2).grid(row=4, column=3)
tv=tkinter.StringVar()
sbox=tkinter.Entry(root, textvariable=tv)
sbox.grid(row=5, column=3)
v = tkinter.IntVar()
tkinter.Radiobutton(root, text='Sohn',width =25, variable=v, value=1).grid(row=6, column=3)
tkinter.Radiobutton(root, text='Tochter',width =25, variable=v, value=2).grid(row=7, column=3)
ttv=tkinter.StringVar()
chname=tkinter.Label(root, text="Name der Kindes:")
chname.grid(row=8, column=2)
cname=tkinter.StringVar()
cn=tkinter.Entry(root, textvariable=cname)
cn.grid(row=8, column=3)
pa=tkinter.Label(root, text="").grid(row=9, column=1)

date2=tkinter.Label(root, text="Datum:")
date2.grid(row=10, column=2)
date=tkinter.Entry(root, textvariable=ttv)
date.grid(row=10, column=3)
fill=tkinter.Label(root, text="")
fill.grid(row=11, column=2)
own=tkinter.Label(root, text="Eigener Name:")
own.grid(row=12, column=2)
tvvv=tkinter.StringVar()
own_name=tkinter.Entry(root, textvariable=tvvv)
own_name.grid(row=12, column=3)
fill2=tkinter.Label(root, text="")
fill2.grid(row=14, column=2)

finish=tkinter.Button(root, text="Fertig", command=exec, width="30", height="2", bg="lightgreen")
finish.grid(row=15, column=3)
root.mainloop()
