import tkinter
from tkinter import *
root=tkinter.Tk()
rw=tkinter.StringVar()
tw=tkinter.Text(root, font=('Calibri', 12))

text=open("Entschuldigung.txt", "r")
t=text.read()
tw.insert(END, t)
def exec():
    print(tw.get(2.6))
    rt=tw.get(2.6)
    import tempfile
    import win32api
    import win32print

    filename = tempfile.mktemp (".txt")
    open (filename, "w").write (tw.get(2.6))
    win32api.ShellExecute (
    0,
    "printto",
    filename,
    '"%s"' % win32print.GetDefaultPrinter (),
    ".",
    0
    )

tw.pack()
prin=tkinter.Button(root, text="Fertig", command=exec)
prin.pack()
root.mainloop()