from tkinter import *
# To load tkinter 'sudo apt install 
root = Tk()
root.title('Simple Calculator')
e=  Entry(root,width=35 ,borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

def clickAdd(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    
    return
def button_add():
    first_number = e.get()
    global f_num
    global math
    math='addition'   
    f_num=int(first_number)
    e.delete(0,END)
    
    return

def button_clear():
    e.delete(0, END)
    return

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,f_num+int(second_number))
    elif math == 'multiply':    
        e.insert(0,f_num*int(second_number))
    elif math == 'substraction':    
        e.insert(0,f_num-int(second_number))
    elif math == 'divide':    
        e.insert(0,f_num/int(second_number))        
           

def button_substract():
    first_number =e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0,END)
    
    return

def button_multiply():
    first_number =e.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(first_number)
    e.delete(0,END)
    
    return

def button_divide():
    first_number =e.get()
    global f_num
    global math
    math = 'divide'
    f_num = int(first_number)
    e.delete(0,END)
    
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
button_0 = Button(root, text='0', padx=40,pady=20,command=lambda:clickAdd(0) ).grid(row=4,column=0)
button_add = Button(root, text='+', padx=40,pady=20,command=button_add).grid(row=5,column=0)
button_clear = Button(root, text='Clear', padx=79,pady=20,command=button_clear ).grid(row=4,column=1,columnspan=2)
button_equal = Button(root, text='=',padx=91,pady=20,command=button_equal).grid(row=5,column=1,columnspan=2)

button_substract = Button(root, text='-', padx=40,pady=20,command=button_substract).grid(row=6,column=0)
button_multiply = Button(root, text='*', padx=40,pady=20,command=button_multiply).grid(row=6,column=1)
button_divide = Button(root, text='/', padx=40,pady=20,command=button_divide).grid(row=6,column=2)


mainloop()