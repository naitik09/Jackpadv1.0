from tkinter import *
import tkinter.messagebox as message
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def New():
    global file
    root.title("Untitled - Jackpad")
    file = None
    textarea.delete(1.0,END)
def Save():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            #save as a new files
            with open(file,'a') as fill:
                foal = fill.write(textarea.get(1.0,END))
                message.showinfo("file saved","Your file is saved")
    else:
        #save as a old files
        with open(file,'a') as fill:
            foal = fill.write(textarea.get(1.0,END))
            message.showinfo("file saved","Your file is saved")

def Open():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file+" - Jackpad"))
        textarea.delete(1.0,END)
        with open(file,'r') as f:
            fi = f.read()
            textarea.insert(1.0,fi)


def Exit():
    root.destroy()
def About():
    message.showinfo("About","Jackpad v1.0\nmade by jack")
def Copy():
    textarea.event_generate(("<<Copy>>"))
def Cut():
    textarea.event_generate(("<<Cut>>"))
def Paste():
    textarea.event_generate(("<<Paste>>"))
# def Undo():
#     textarea.event_generate(("<<Undo>>"))
def Select():
    pass
def Gray():
    pass
def Black():
    pass
def White():
    pass
if __name__ == "__main__":
    root = Tk()
    root.title('Untitled - Jackpad')
    root.call('wm','iconphoto',root._w,PhotoImage(file='1.png'))
    root.geometry("640x400")
    filemenu = Menu(root)
    option = Menu(filemenu,tearoff=0)
    option.add_command(label="New",command=New)
    option.add_command(label="Open",command=Open)
    option.add_command(label="Save",command=Save)
    option.add_command(label="Exit",command=Exit)
    filemenu.add_cascade(label="File",menu=option)
    option2 = Menu(filemenu,tearoff=0)
    option2.add_command(label="Copy",command=Copy)
    option2.add_command(label="Paste",command=Paste)
    option2.add_command(label="Cut",command=Cut)
    #option2.add_command(label="Undo",command=Undo)
    option2.add_command(label="Select All",command=Select)
    filemenu.add_cascade(label="Edit",menu=option2)
    option3 = Menu(filemenu,tearoff=0)
    back = Menu(option3,tearoff=0)

    back.add_command(label="Gray",command=Gray)
    back.add_command(label="Black",command=Black)
    back.add_command(label="White",command=White)
    option3.add_cascade(label='Theme',menu=back)

    filemenu.add_cascade(label="Preference",menu=option3)
    filemenu.add_command(label="About",command=About)
    frame = Frame(root)
    textarea = Text(frame,font='lucida 15')
    file = None
    textarea.pack(expand=True,fill=BOTH)
    frame.pack(expand=True,fill=BOTH)
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    root.config(menu=filemenu)
    root.mainloop()
from tkinter import *
import tkinter.messagebox as message
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def New():
    global file
    root.title("Untitled - Jackpad")
    file = None
    textarea.delete(1.0,END)
def Save():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            #save as a new files
            with open(file,'a') as fill:
                foal = fill.write(textarea.get(1.0,END))
                message.showinfo("file saved","Your file is saved")
    else:
        #save as a old files
        with open(file,'a') as fill:
            foal = fill.write(textarea.get(1.0,END))
            message.showinfo("file saved","Your file is saved")

def Open():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file+" - Jackpad"))
        textarea.delete(1.0,END)
        with open(file,'r') as f:
            fi = f.read()
            textarea.insert(1.0,fi)


def Exit():
    root.destroy()
def About():
    message.showinfo("About","Jackpad v1.0\nmade by jack")
def Copy():
    textarea.event_generate(("<<Copy>>"))
def Cut():
    textarea.event_generate(("<<Cut>>"))
def Paste():
    textarea.event_generate(("<<Paste>>"))
# def Undo():
#     textarea.event_generate(("<<Undo>>"))
def Select():
    pass
def Gray():
    pass
def Black():
    pass
def White():
    pass
if __name__ == "__main__":
    root = Tk()
    root.title('Untitled - Jackpad')
    root.call('wm','iconphoto',root._w,PhotoImage(file='1.png'))
    root.geometry("640x400")
    filemenu = Menu(root)
    option = Menu(filemenu,tearoff=0)
    option.add_command(label="New",command=New)
    option.add_command(label="Open",command=Open)
    option.add_command(label="Save",command=Save)
    option.add_command(label="Exit",command=Exit)
    filemenu.add_cascade(label="File",menu=option)
    option2 = Menu(filemenu,tearoff=0)
    option2.add_command(label="Copy",command=Copy)
    option2.add_command(label="Paste",command=Paste)
    option2.add_command(label="Cut",command=Cut)
    #option2.add_command(label="Undo",command=Undo)
    option2.add_command(label="Select All",command=Select)
    filemenu.add_cascade(label="Edit",menu=option2)
    option3 = Menu(filemenu,tearoff=0)
    back = Menu(option3,tearoff=0)

    back.add_command(label="Gray",command=Gray)
    back.add_command(label="Black",command=Black)
    back.add_command(label="White",command=White)
    option3.add_cascade(label='Theme',menu=back)

    filemenu.add_cascade(label="Preference",menu=option3)
    filemenu.add_command(label="About",command=About)
    frame = Frame(root)
    textarea = Text(frame,font='lucida 15')
    file = None
    textarea.pack(expand=True,fill=BOTH)
    frame.pack(expand=True,fill=BOTH)
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    root.config(menu=filemenu)
    root.mainloop()

