#ZOE ENGEL, CLASS 1

from tkinter import *
from random import sample
from datetime import *
from tkinter import messagebox


window = Tk()
window.title("Ithuba lottery app")
window.geometry("640x400")
window.config(bg="orange")

# WINDOW NAME
name_lbl = Label(window, text="ITHUBA LOTTERY GAME", font=28)
name_lbl.place(x=80, y=5)

# NAME LABEL AND ENTRY
name_lbl = Label(window, text="Name:", font=20)
name_entry = Entry(window)
name_lbl.place(x=23 ,y=50)
name_entry.place(x=90, y=50)
surname_lbl = Label(window, text="Surname:", font=20)
surname_lbl.place(x=290,y=50)
surname_entry = Entry(window)
surname_entry.place(x=380, y=50)

# GENERATING SIX RANDOM NUMBERS
my_numbers = []
lotto = sample(range(0, 50), 6)
lotto.sort()
print(lotto)

# ADDING THE DATE
current_date = datetime.now()
mydate_lbl = Label(window)
mydate_lbl.config(text="Today's date: " + current_date.strftime("%d-%m-%y %H:%M"))
mydate_lbl.place(x=399, y=5)

# ENTRIES LABEL
entry_lbl = Label(window, font=20, text="Please enter your lotto entries: ")
entry_lbl.place(x=30, y=120)

# CREATING ENTRIES
entry1 = Entry(window, width=4, justify='center')
entry1.place(x=40, y=150)
entry2 = Entry(window, width=4, justify='center')
entry2.place(x=80, y=150)
entry3 = Entry(window, width=4, justify='center')
entry3.place(x=120, y=150)
entry4 = Entry(window, width=4, justify='center')
entry4.place(x=160, y=150)
entry5 = Entry(window, width=4, justify='center')
entry5.place(x=200, y=150)
entry6 = Entry(window, width=4, justify='center')
entry6.place(x=240, y=150)


# CREATING A FUNCTION TO CHECK FOR MATCHES BETWEEN LOTTO NUMBERS AND ENTRIES
def check():
    try:
        my_numbers.append(int(entry1.get()))
        my_numbers.append(int(entry2.get()))
        my_numbers.append(int(entry3.get()))
        my_numbers.append(int(entry4.get()))
        my_numbers.append(int(entry5.get()))
        my_numbers.append(int(entry6.get()))

        matches = 0
        for i in my_numbers:
            if i in lotto:
                matches += 1

        if matches == 0:
                result_lbl.config(text="Better luck next time!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
        elif matches == 1:
                result_lbl.config(text="Better luck next time!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
        elif matches == 2:
                result_lbl.config(text="YOU WON R20.00!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
        elif matches == 3:
                result_lbl.config(text="YOU WON R100.50!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
        elif matches == 4:
                result_lbl.config(text="YOU WON R2 384.00!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
        elif matches == 5:
                result_lbl.config(text="YOU WON R8 584.00" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
        elif my_numbers == lotto:
                result_lbl.config(text="YOU'VE WON THE JACKPOT of R10,000 000.00!!" + "\n" + str(lotto))

    except ValueError:
        messagebox.showinfo("ERROR","Please enter a valid input")
        entry1.delete(0,END)
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0,END)
        entry5.delete(0,END)
        entry6.delete(0,END)



# ADDING THE TEXT INTO A FILE (FILE HANDLING)
    lotto_txt = open("Lotto.txt", "w+")
    lotto_txt.write(result_lbl.cget("text"))
    lotto_txt.write(name_entry.cget("text"))

# CREATING A CHECK BUTTON
check_btn = Button(window, command=check, text="Check lotto", bg="lime")
check_btn.place(x=40, y=180, width=240 )
# check_btn.config(bg="lime")


# EXIT FUNCTION
def exit():
    lors= messagebox.askyesno(title="Message",message= "Are you sure you want to exit?")
    if lors == True:
        window.destroy()
    else:
        return None

# CREATING A RESULT LABEL
result_lbl = Label(window)
result_lbl.place(x=50, y=250)

# CREATING AN EXIT BUTTON
ext_btn = Button(window, command=exit, text="Exit")
ext_btn.place(x=450, y=180, width=99)
ext_btn.config(bg="red")

window.mainloop()
