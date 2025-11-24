from tkinter import *

import customtkinter

from src.receipt_tracker import Transactions
from src.CTkDatePicker import CTkDatePicker

def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("400x800")
app.title("Receipt Tracker")


date_picker = CTkDatePicker(app)
date_picker.set_allow_change_month(False)
date_picker.set_change_months("sub", 5)
date_picker.pack(padx =20, pady=20)

payee_textbox = customtkinter.CTkTextbox(app)
payee_textbox.configure(width=300, height=50, border_spacing=10)
payee_textbox.insert("0.0", "Payee Name")  # insert at line 0 character 0
payee = payee_textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
payee_textbox.pack(padx=10, pady=10)

# payee_textbox.delete("0.0", "end")  # delete all text
# payee_textbox.configure(state="disabled")  # configure textbox to be read-only

category_textbox = customtkinter.CTkTextbox(app)
category_textbox.insert("0.0", "Pick a Category")  # insert at line 0 character 0
category = category_textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
category_textbox.pack(padx=20, pady=20)

amount_textbox = customtkinter.CTkTextbox(app)
amount_textbox.insert("0.0", "$0.00")
amount = amount_textbox.get("0.0","end")
amount_textbox.pack(padx=20, pady=20)

description_textbox = customtkinter.CTkTextbox(app)
description_textbox.insert("0.0", "$0.00")
description = description_textbox.get("0.0","end")
description_textbox.pack(padx=20, pady=20)

project_textbox = customtkinter.CTkTextbox(app)
project_textbox.insert("0.0", "$0.00")
project = project_textbox.get("0.0","end")
project_textbox.pack(padx=20, pady=20)

notes_textbox = customtkinter.CTkTextbox(app)
notes_textbox.insert("0.0", "$0.00")
notes = notes_textbox.get("0.0","end")
notes_textbox.pack(padx=20, pady=20)

link_textbox = customtkinter.CTkTextbox(app)
link_textbox.insert("0.0", "$0.00")
link  = link_textbox.get("0.0","end")
link_textbox.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()
