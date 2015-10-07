__author__ = 'demi'

#myCalculator_expt.py

from tkinter import *
from decimal import *

# key/button click function
def click(key):
    display.insert(END, key)

##### main:
window = Tk()
window.title("My Calc")

# Create top_row Frame
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# use Entry Widget for an Editable Display
display = Entry(top_row, width=45, bg="light green")
display.grid()

# Create num_pad_frame
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

# Provide List of Keys for Number Pad
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']

# Create the buttons with a loop
r = 0   #row counter
c = 0   #column counter

for btn_text in num_pad_list:
    Button(num_pad, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c=c+1
    if c > 2:
        c=0
        r = r+1

# Create the operator Frame (side panel on calc with additional functions (*,%,/,etc)
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    ]

# Create the operator Buttons with a loop
r=0
c=0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c=c+1
    if c > 1:
        c=0
        r=r+1

#Create bottom_row Frame for Large Button
bottom_row = Frame(window)
bottom_row.grid(row=6, column=0, columnspan=2)

#Create large button
btn_text = "CLEAR"
btn_clear = Button(bottom_row, text=btn_text, width=45, command=click).grid(row=1, column=0)


##### Run MainLoop
window.mainloop()

