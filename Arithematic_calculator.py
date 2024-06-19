

from tkinter import *

# Function to update the expression in the entry field
def press(num):
  global expression
  expression = expression + str(num)
  equation.set(expression)

# Function to evaluate the expression
def equalpress():
  global expression
  try:
    result = str(eval(expression))
    equation.set(result)
    expression = result
  except:
    equation.set("Error")
    expression = ""

# Function to clear the entry field
def clear():
  global expression
  expression = ""
  equation.set("")

# Main
expression = ""
window = Tk()
window.title("Simple Calculator")
window.geometry("270x150")

equation = StringVar()
equation_field = Entry(window, textvariable=equation, bd=5)
equation_field.grid(columnspan=4, ipadx=70)

button1 = Button(window, text='1', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(window, text='2', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(window, text='3', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(window, text='+', command=lambda: press("+"), height=1, width=7)
button4.grid(row=2, column=3)

button5 = Button(window, text='4', command=lambda: press(4), height=1, width=7)
button5.grid(row=3, column=0)

button6 = Button(window, text='5', command=lambda: press(5), height=1, width=7)
button6.grid(row=3, column=1)

button7 = Button(window, text='6', command=lambda: press(6), height=1, width=7)
button7.grid(row=3, column=2)

button8 = Button(window, text='-', command=lambda: press("-"), height=1, width=7)
button8.grid(row=3, column=3)

button9 = Button(window, text='7', command=lambda: press(7), height=1, width=7)
button9.grid(row=4, column=0)

button10 = Button(window, text='8', command=lambda: press(8), height=1, width=7)
button10.grid(row=4, column=1)

button11 = Button(window, text='9', command=lambda: press(9), height=1, width=7)
button11.grid(row=4, column=2)

button12 = Button(window, text='*', command=lambda: press("*"), height=1, width=7)
button12.grid(row=4, column=3)

button13 = Button(window, text='0', command=lambda: press(0), height=1, width=7)
button13.grid(row=5, column=0)

button14 = Button(window, text='=', command=equalpress, height=1, width=7)
button14.grid(row=5, column=1)

button15 = Button(window, text='C', command=clear, height=1, width=7)
button15.grid(row=5, column=2)

button16 = Button(window, text='/', command=lambda: press("/"), height=1, width=7)
button16.grid(row=5, column=3)

window.mainloop()

