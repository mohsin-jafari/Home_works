from tkinter import*
from tkinter import messagebox

#backent
def clear_field():
    day1_entry.delete(0,"end")
    month1_entry.delete(0,"end")
    year1_entry.delete(0,"end")
    day2_entry.delete(0,"end")
    month2_entry.delete(0,"end")
    year2_entry.delete(0,"end")
    label.config(bg = "light pink", text = "")

def check_error():
    items = [day1_entry.get(),month1_entry.get(),year1_entry.get(),day2_entry.get(),month2_entry.get(),year2_entry.get()]
    for i in items:
        if not i.isdigit():
            return False

def calculate():
    if check_error() == False:
        clear_field()
        messagebox.showerror("INPUT ERROR")
        return
    else:
        day1 = int(day1_entry.get())
        month1 = int(month1_entry.get())
        year1 = int(year1_entry.get())
        day2 = int(day2_entry.get())
        month2= int(month2_entry.get())
        year2 = int(year2_entry.get())
        months = [31,31,31,31,31,31,30,30,30,30,30,30]
        if day2 < day1:
            day2 += months[month2 - 1]
            month2 -= 1
        if month2 < month1:
            month2 += 12
            year2 -= 1
        result = "resultant age\n\n" + "Year : " + str(year2 - year1) + "\nmonth : " + str(month2 - month1) + "\nDay : " + str(day2 - day1)
        label.config(bg = "light grey", text = result)
        
    
        
    




#frontent
window = Tk()
window.title("Age Finder")
window.geometry("600x700+40+240")
window.resizable(False,False)
window.config(bg = "light pink")
#two widget for birthday and given date
birthday = Label(window, text = "Date of birth",font = ("Poppins bold",10),bg = "light pink")
birthday.place(y = 36,x = 30)

given_date = Label(window, text = "Given date",font = ("Poppins bold",10),bg = "light pink")
given_date.place(y = 36,x = 370)

#widget for day month year
day1 = Label(window,text = "Day",font = ("Arial",9),bg = "light pink", width= 5)
day1.place(y = 106,x = 8)

day1_entry = Entry(window,font = ("Arial",8),bd = 3, width = 7)
day1_entry.place(y = 106,x = 110)

month1 = Label(window,text = "Month",font = ("Arial",9),bg = "light pink", width= 5)
month1.place(y = 160,x = 8)

month1_entry = Entry(window,font = ("Arial",8),bd = 3, width = 7)
month1_entry.place(y = 160,x = 110)

year1 = Label(window,text = "Year",font = ("Arial",9),bg = "light pink", width= 5)
year1.place(y = 214,x = 8)

year1_entry = Entry(window,font = ("Arial",8),bd = 3, width = 7)
year1_entry.place(y = 214,x = 110)


day2 = Label(window,text = "Day",font = ("Arial",9),bg = "light pink", width= 5)
day2.place(y = 106,x = 318)

day2_entry = Entry(window,font = ("Arial",8),bd = 3, width = 7)
day2_entry.place(y = 106,x = 420)

month2 = Label(window,text = "Month",font = ("Arial",9),bg = "light pink", width= 5)
month2.place(y = 160,x = 318)

month2_entry = Entry(window,font = ("Arial",8),bd = 3, width = 7)
month2_entry.place(y = 160,x = 420)

year2 = Label(window,text = "Year",font = ("Arial",9),bg = "light pink", width= 5)
year2.place(y = 214,x = 318)

year2_entry = Entry(window,font = ("Arial",8),bd = 3, width = 7)
year2_entry.place(y = 214,x = 420)

#two button for calculate and clear field
cal = Button(window, text = "Calculate", width = 6,bd = 2, command = calculate)
cal.place(y = 310,x = 210)

clear = Button(window, text = "Clear field", width = 6,bd = 2, command = clear_field)
clear.place(y = 377,x = 210)

label = Label(window,bg = "light pink", width = 18, height = 6)
label.place(y = 460,x = 142)
window.mainloop()
            