from tkinter import *
buttons = ["7","8","9","+",
                    "4","5","6"," -",
                    "1","2","3","÷",
                    " (","0"," )","*",
                    "C","B"," , ","=" ]
question = ""                   
def clear_field():
    global question 
    question = ""
    text.delete(1.0,"end")
def back():
    global question 
    question = question[0:len(question) - 1]
    text.delete(1.0,"end")
    text.insert(1.0, question)
def solve():
    global question 
    try:
        result = str(eval(question))
        question = result
        text.delete(1.0,"end")
        text.insert(1.0, question)
    except:
        clear_field()
        text.insert(1.0,"Error")

def cancatenate(sym):
    global question 
    sym = "-" if sym == " -" else "/" if sym == "÷" else "(" if sym == " (" else ")" if sym == " )" else "." if sym == " , " else sym
    question += sym
    text.delete(1.0,"end")
    text.insert(1.0, question)

window = Tk()
window.title("Simple Calculator")
window.geometry("578x680+50+300")
window.resizable(False, False)
text = Text(window,bg = 'black',fg = "light green", height = 2, width = 19, font =("Arial",14))
text.grid(row = 0, column= 0, columnspan = 4)
row = 1
col = 0
for i in buttons:
    button = Button(window, text = i,bd = 3,pady = 31,padx = 56,fg = "blue" if i in ["+"," -","*","÷","B","C","="," , "] else "black", command = clear_field if i == "C" else back if i == "B" else solve if i == "=" else lambda tex = i: cancatenate(tex),bg = "red" if i == "=" else "light grey")
    button.grid(row = row, column = col)
    col += 1
    if col == 4:
        row += 1
        col = 0

window.mainloop()