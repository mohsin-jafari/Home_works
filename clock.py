from tkinter import *
import time 
def timer():
    h = time.strftime("%H")
    m = time.strftime("%M")
    sec = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    result = h + " : " + m + " : " + sec + " " + am_pm + "\n" + day
    label.config(text = result)
    
    label.after(1000, timer)
window = Tk()
window.title("Clock")
label = Label(window,bd = 2, width= 20, height = 2)
label.pack()
timer()
window.mainloop()