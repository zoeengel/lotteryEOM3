# ZOE ENGEL, CLASS 1

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Age Verification")
window.geometry("300x190")
window.config(bg="orange")

# # NAME LABEL AND ENTRY
# name_lbl = Label(window, text="Name:", font=20)
# name_entry = Entry(window)
# name_lbl.pack(side=TOP)
# name_entry.pack(side=TOP)
# surname_lbl = Label(window, text="Surname:", font=20)
# surname_lbl.pack(side=TOP)
# surname_entry = Entry(window)
# surname_entry.pack(side=TOP)

# AGE LABEL AND ENTRY
age_lbl = Label(window, text="Enter your age:" , font=20)
age_entry = Entry(window, width=5)
age_lbl.pack(side=TOP)
age_entry.pack(side=TOP)

# AGE CHECKING FUNCTION
def ageCheck():
    try:
        age = int(age_entry.get())
        if age < 18:
             raise ValueError(messagebox.showinfo("ERROR","You need to be 18 years or older to play the lottery!"))
        elif type(age) != int:
            raise ValueError(messagebox.showerror("Enter a valid input"))

    # except ValueError as e:
    #     print(e)
    #     age_entry.delete(0, END)
    except ValueError:
        messagebox.showinfo("ERROR","Enter a valid input")
        window.destroy()
    else:
            messagebox.showinfo('Message',"Get ready to play the Lotto!")
            age_entry.delete(0, END)
            window.withdraw()
            import real
            real.real()

# SUBMIT BUTTON
HEIGHT = 1
WIDTH = 12
submit_btn = Button(window, text="Submit", width=WIDTH, height=HEIGHT, command=ageCheck)
submit_btn.config(bg="yellow")
submit_btn.pack(side=TOP)

window.mainloop()
