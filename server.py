from tkinter import *
from tkinter import messagebox
from data import names_girls
import pandas as pd
import send_results

# Functions
def date_to_csv(list, who_vote):
    new_table_to_csv = pd.DataFrame(list)
    table_name = f"rated_names_{who_vote.lower()}.csv"
    print(table_name)
    new_table_to_csv.to_csv(table_name, index=False)

    send_results.send_csv(filename=table_name, name=who_vote)

# Variables
name_default_num = 0
total_names_num = len(names_girls)
names_data = []

def save():
    global name_default_num, total_names_num
    next_name_value = names_girls[name_default_num]
    name_value.config(text=next_name_value)
    choice = who_vote_choice.get()
    rate_to_add = rate_var.get()
    # Check if parent is set as Select
    if choice == "Select":
        messagebox.showinfo(title="Info", message="Per favore, scegli chi valuta")
        name_default_num = 0
        name_value.config(text=names_girls[name_default_num])
    else:
        name_add = {
            "parent": choice,
            "name": next_name_value,
            "rate": rate_to_add
        }
        names_data.append(name_add)

        # Update name label after saving the data
        name_default_num += 1
        try:
            name_value.config(text=names_girls[name_default_num])
        except IndexError:
            name_value.config(text="La lista e finita")
        total_names_num -= 1
        name.config(text=f"Nomi rimasti: {total_names_num}")

    if name_default_num >= len(names_girls):
        date_to_csv(names_data, choice)
        messagebox.showinfo(title="Info", message="File e pronto.")


# ---------------------------------- UI Setup ----------------------------------
window = Tk()
window.title("Baby's Name")
window.config(padx=50, pady=50)

# Creating canvas
canvas = Canvas(width=400, height=400)
baby_img = PhotoImage(file="images/little-baby.png")
canvas.create_image(200, 200, image=baby_img)
canvas.grid(column=0, row=0, columnspan=3)

# Labels
who_vote = Label(text="Chi c'è? Mamma o papa?")
who_vote.grid(column=0, row=1)
name = Label(text=f"Nomi nella lista: {total_names_num}", pady=10)
name.grid(column=0, row=2)
rating = Label(text="Ti piace questo nome? Voto da 1 a 10.")
rating.grid(column=2, row=2)
name_value = Label(text=names_girls[0])
name_value.config(font=('Helvatical bold',30))
name_value.grid(column=0, row=3)

# Option menu. List of users
option_list = ("Mamma", "Papa", "Zia", "Nonna")
who_vote_choice = StringVar()
who_vote_choice.set("Select")
opt_menu = OptionMenu(
    window,
    who_vote_choice,
    *option_list
)
opt_menu.grid(column=2, row=1)

# Scale widget. Estimation by each user
rate_var = IntVar()
rating_scale = Scale(
    window,
    variable=rate_var,
    from_=0,
    to=10,
    orient=HORIZONTAL,
    sliderlength=15
)
rating_scale.grid(column=2, row=3)

# Buttons
next_name_btn = Button(text="Prossimo nome", command=save, width=30, highlightthickness=10)
next_name_btn.grid(column=0, row=5, columnspan=3)

#TODO 1. Translate all labels to italian

window.mainloop()