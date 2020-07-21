from tkinter import *

root = Tk()
root.title('Simple Calculator')
root.iconbitmap("images/Colins Logo2.ico")

button_font = ('Helvetica', 14, 'bold')
off_white = '#F6F6F6'
off_black = '#151515'
operator_color = '#A6EEEE'

calc = LabelFrame(root, padx=5, pady=5, bd=5, bg=off_black, relief=FLAT)
calc.grid(row=1, column=0)
e = Entry(calc, width=31, bd=10, relief=FLAT, bg='#333', fg=off_white, font=button_font)
e.grid(row=0, column=0, columnspan=5, padx=1, pady=20)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    do_this = e.get()
    e.delete(0, END)
    if '+' in do_this:
        do_this = do_this.split('+')
        answer = float(do_this[0]) + float(do_this[1])
    if '-' in do_this:
        do_this = do_this.split('-')
        answer = float(do_this[0]) - float(do_this[1])
    if '*' in do_this or 'x' in do_this:
        if '*' in do_this:
            do_this = do_this.split('*')
        else:
            do_this = do_this.split('x')
        answer = float(do_this[0]) * float(do_this[1])
    if '/' in do_this or '÷' in do_this:
        if '/' in do_this:
            do_this = do_this.split('/')
        else:
            do_this = do_this.split('÷')
        answer = float(do_this[0]) / float(do_this[1])
    e.insert(0, answer)

# Define buttons
button_1 = Button(calc, text='1', padx=30, pady=20, command=lambda: button_click(1), bg=off_white, font=button_font)
button_2 = Button(calc, text='2', padx=30, pady=20, command=lambda: button_click(2), bg=off_white, font=button_font)
button_3 = Button(calc, text='3', padx=30, pady=20, command=lambda: button_click(3), bg=off_white, font=button_font)
button_4 = Button(calc, text='4', padx=30, pady=20, command=lambda: button_click(4), bg=off_white, font=button_font)
button_5 = Button(calc, text='5', padx=30, pady=20, command=lambda: button_click(5), bg=off_white, font=button_font)
button_6 = Button(calc, text='6', padx=30, pady=20, command=lambda: button_click(6), bg=off_white, font=button_font)
button_7 = Button(calc, text='7', padx=30, pady=20, command=lambda: button_click(7), bg=off_white, font=button_font)
button_8 = Button(calc, text='8', padx=30, pady=20, command=lambda: button_click(8), bg=off_white, font=button_font)
button_9 = Button(calc, text='9', padx=30, pady=20, command=lambda: button_click(9), bg=off_white, font=button_font)
button_0 = Button(calc, text='0', padx=30, pady=20, command=lambda: button_click(0), bg=off_white, font=button_font)
button_point = Button(calc, text='.', padx=33, pady=20, command=lambda: button_click('.'), bg=off_white, font=button_font)
button_add = Button(calc, text='+', padx=30, pady=20, command=lambda: button_click('+'), bg=operator_color, font=button_font)
button_subtract = Button(calc, text='-', padx=32, pady=20, command=lambda: button_click('-'), bg=operator_color, font=button_font)
button_multiply = Button(calc, text='x', padx=30, pady=20, command=lambda: button_click('*'), bg=operator_color, font=button_font)
button_divide = Button(calc, text='÷', padx=30, pady=20, command=lambda: button_click('/'), bg=operator_color, font=button_font)
button_equal = Button(calc, text='=', padx=168, pady=10, command=button_equal, bg='#FFB533', font=button_font)
button_clear = Button(calc, text='C', padx=28, pady=20, command=button_clear, bg= '#FF8888', font=button_font)

# Put the buttons on the screen
button_7.grid(row=1, column=0, pady=2)
button_8.grid(row=1, column=1, pady=2)
button_9.grid(row=1, column=2, pady=2)
button_divide.grid(row=1, column=3, pady=2)

button_4.grid(row=2, column=0, pady=2)
button_5.grid(row=2, column=1, pady=2)
button_6.grid(row=2, column=2, pady=2)
button_multiply.grid(row=2, column=3, pady=2)

button_1.grid(row=3, column=0, pady=2)
button_2.grid(row=3, column=1, pady=2)
button_3.grid(row=3, column=2, pady=2)
button_subtract.grid(row=3, column=3, pady=2)

button_clear.grid(row=4, column=0, pady=2)
button_0.grid(row=4, column=1, pady=2)
button_point.grid(row=4, column=2, pady=2)
button_add.grid(row=4, column=3, pady=2)

button_equal.grid(row=5, column=0, columnspan=4, pady=2)

root.mainloop()