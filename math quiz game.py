from tkinter import*
import random


class Question:
    def __init__(self):
        self.x = str(random.randint(0,15))
        self.y = str(random.randint(0,15))
        self.symbol = random.choice(["+","-","*"])
    def answer(self):
        return int(eval(self.x + self.symbol + self.y))
    def __str__(self):
        return f"{self.x} {self.symbol} {self.y} =?"

score = 0
_str = ""
i = 10
round = 0

def close_window():
    window.destroy()
    
def guide():
    for widget in window.winfo_children():
        widget.destroy()
    help = Label(window, text = "total question : 10\ntota score : 20\nfor answer one question you have 10sec\none question have 2 mark",bg = "light green", height= 6)
    help.pack()
    button = Button(window, text = "back", command = menu,bg = "light green",bd = 2)
    button.pack()

def menu():
    for widget in window.winfo_children():
        widget.destroy()
    start = Button(window, text = "Start Game", font = ("Poppins bold",8),bd = 2, width = 9, command = start_game,bg = "light green")
    start.place(y = 164,x = 172)
#button for display help
    help = Button(window, text = "Help", font = ("Poppins bold",8),bd = 3, width = 9,bg = "light green", command = guide)
    help.place(y = 233,x = 172)
#creating button for quit
    quit = Button(window, text = "Quit", font = ("Poppins bold",8),bd = 2, width = 9, command = close_window,bg = "light green")
    quit.place(y = 302,x = 172)
    
    
    
       
          

                 
          
    
def start_game():
    global round
    global score
    global i
    i = 10
    quiz = Question()
                
    round += 1
    
    if round == 11:
        
        for widget in window.winfo_children():
            widget.destroy()
            
        result = Label(window, text = f"total score : 20\nyour score : {score}", font = ("Poppins bold",14),bg = "light green")
        result.place(y = 300,x = 124)
        
        but1 = Button(window, text = "Play Again",bd = 2,bg = "light green", width= 12, command = start_game)
        but1.place(y = 464,x = 170)
        
        but2 = Button(window, text = "Main Menu",bd = 2,bg = "light green", width = 12, command = menu)
        but2.place(y = 530,x = 170)
        round = 0
        score = 0
        return
        
    #functions
    def back():
        global _str
        _str = _str[:len(_str) - 1]
        text.delete(1.0,"end")
        text.insert(1.0,_str)
    def can(sym):
        global _str
        _str += sym if sym != "-" else "-" if _str == "" else ""
        text.delete(1.0,"end")
        text.insert(1.0,_str)

    def submit():
        global score
        global _str
        if _str == "":
            pass
        else:
            if int(_str) == quiz.answer():
                label.config(text = "Perfect")
                score += 2
                _str = ""
                label.after(1000,start_game)
            else:
                label.config(text = "Wrong answer")
                _str = ""
                label.after(1000,start_game)
              
              
              
        
    
    #buttons
    for widget in window.winfo_children():
        widget.destroy()
        time = Label(window,bg = "light green")
    time.place(y = 10,x = 510)
    label = Label(window,bg = "light green", width = 14,bd = 3, text = str(quiz),font = ("Arial",14), height = 2)
    label.pack()
    text = Text(window,bg = "black",fg = "red", height = 1, font = ("Arial",16), width =10,bd = 3)
    text.place(x = 122,y = 120)
    
    
    button_7 = Button(window, text = "7",bd = 2, font = ("Poppins bold",10),padx = 86,pady = 32, command = lambda : can("7"))
    button_7.place(y = 208)

    button_4 = Button(window, text = "4",bd = 2, font = ("Poppins bold",10),padx = 86,pady = 36, command = lambda : can("4"))
    button_4.place(y = 327)

    button_1 = Button(window, text = "1",bd = 2, font = ("Poppins bold",10),padx = 86,pady = 36, command = lambda : can("1"))
    button_1.place(y = 454)    
    
    button_b = Button(window, text = "X",bd = 2, font = ("Poppins bold",10),padx = 84,pady = 32, command = back)
    button_b.place(y = 580)


    button_8 = Button(window, text = "8",bd = 2, font = ("Poppins bold",10),padx = 86,pady = 32,command = lambda : can("8"))
    button_8.place(y = 208,x = 202)

    button_5 = Button(window, text = "5",bd = 2, font = ("Poppins bold",10),padx = 86,pady = 36, command = lambda : can("5"))
    button_5.place(y = 327,x = 202)

    button_2 = Button(window, text = "2",bd = 2, font = ("Poppins bold",10),padx = 86,pady = 36, command = lambda : can("2"))
    button_2.place(y = 454,x = 202)    
    
    button_0 = Button(window, text = "0",bd = 2, font = ("Poppins bold",10),padx = 37,pady = 32, command = lambda : can("0"))
    button_0.place(y = 580,x = 202)

    button_sign = Button(window, text = "-",bd = 2, font = ("Poppins bold",10),padx = 38,pady = 32, command = lambda : can("-"))
    button_sign.place(y = 580,x = 306)



    button_9 = Button(window, text = "9",bd = 2, font = ("Poppins bold",10),padx = 84,pady = 32, command = lambda : can("9"))
    button_9.place(y = 208,x = 403)

    button_6 = Button(window, text = "6",bd = 2, font = ("Poppins bold",10),padx = 84,pady = 36, command = lambda : can("6"))
    button_6.place(y = 327,x = 403)

    button_3 = Button(window, text = "3",bd = 2, font = ("Poppins bold",10),padx = 84,pady = 36, command = lambda : can("3"))
    button_3.place(y = 454,x = 403)    
    
    button_e = Button(window, text = "Enter",bd = 2, font = ("Poppins bold",10),padx = 84,pady = 32, width = 1, command = submit)
    button_e.place(y = 580,x = 403)
    def timer():
        global i
        if i == 0:           
            return
        time.config(text =f"{0:02d}:{i:02d}")
        i-= 1
        time.after(1000,timer)
        
      
    timer()
    
    
    label.after(10000,start_game)
    
    
    
    
    
    
    
    
    
   

        

window = Tk()
window.title("math quiz game")
window.geometry("600x700")
window.config(bg = "light green")
menu()
window.mainloop()