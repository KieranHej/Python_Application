from tkinter import *
import tkinter.messagebox

def myfunt(a):
    print("Hello this is my function ", a)

root = Tk()
root.title('test')
menu = Menu(root)
root.config(menu=menu)
sub1 = Menu(menu)
menu.add_cascade(label="Drop Down Menu Test",menu=sub1)
sub1.add_command(label="Hello", command=myfunt)

toolbar = Frame(root, bg='blue')
label = Label(toolbar, text='My Toolbar')
b1 = Button(toolbar, text='Hello', command=myfunt)
b1.pack(side=LEFT, padx=2, pady=5)
toolbar.pack(side=TOP, fill=X)
label.pack()


status = Label(root, text='Waiting to compute', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


canvas = Canvas(root, width=200, heigh=200)
canvas.create_line(20,20,20,120)
canvas.create_rectangle(20,20, 200, 800)
canvas.delete()

photo = PhotoImage(file='/Users/bssmvh/Desktop/cvs/tumour.png')
label = Label(root, image=photo)
label.pack()

canvas.pack()
root.mainloop()