from tkinter import *
# To load tkinter 'sudo apt install 
root = Tk()
root.title('Simple Calculator')
e=  Entry(root, width=35 ,borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

def clickAdd():
    return
button_7 = Button(root, text='7', padx=40,pady=20 ,command=lambda:clickAdd(7)).grid(row=1,column=0)
button_8 = Button(root, text='8', padx=40,pady=20,command=lambda:clickAdd(8) ).grid(row=1,column=1)
button_9 = Button(root, text='9', padx=40,pady=20,command=lambda:clickAdd(9) ).grid(row=1,column=2)
button_4 = Button(root, text='4', padx=40,pady=20,command=lambda:clickAdd(4) ).grid(row=2,column=0)
button_5 = Button(root, text='5', padx=40,pady=20,command=lambda:clickAdd(5) ).grid(row=2,column=1)
button_6 = Button(root, text='6', padx=40,pady=20,command=lambda:clickAdd(6) ).grid(row=2,column=2)
button_1 = Button(root, text='1', padx=40,pady=20,command=lambda:clickAdd(1) ).grid(row=3,column=0)
button_2 = Button(root, text='2', padx=40,pady=20,command=lambda:clickAdd(2) ).grid(row=3,column=1)
button_3 = Button(root, text='3', padx=40,pady=20,command=lambda:clickAdd(3) ).grid(row=3,column=2)


mainloop()