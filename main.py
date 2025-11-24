from tkinter import *

import customtkinter

from src.receipt_tracker import Transactions
from src.CTkDatePicker import CTkDatePicker

def button_callback():
    print("button clicked")

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

app = customtkinter.CTk()
app.geometry("400x800")
app.title("Receipt Tracker")

date_picker = CTkDatePicker(app)
date_picker.set_allow_change_month(False)
date_picker.set_change_months("sub", 5)
date_picker.pack(padx =20, pady=5)

amount_textbox = customtkinter.CTkEntry(app, placeholder_text="0.00")
amount_textbox.pack(padx=20, pady=5)

payee_textbox = customtkinter.CTkEntry(app,placeholder_text="Payee")
# payee_textbox.configure(width=300, height=50, border_spacing=10)
payee_textbox.pack(padx=10, pady=10)

category_var = customtkinter.StringVar(value="option 2")
category_combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"], command=combobox_callback)
category_combobox.set("option 2")
category_combobox.pack(padx=20, pady=5)

project_var = customtkinter.StringVar(value="option 2")
project_combobox = customtkinter.CTkComboBox(app, values=["Project 1", "Project 2"], command=combobox_callback)
project_combobox.pack(padx=20, pady=5)

description_textbox = customtkinter.CTkEntry(app, placeholder_text="Description of expense")
description_textbox.pack(padx=20, pady=5)

link_textbox = customtkinter.CTkEntry(app, placeholder_text="link")
link_textbox.pack(padx=20, pady=5)

notes_textbox = customtkinter.CTkTextbox(app)
notes_textbox.insert("0.0", "Notes...")
notes = notes_textbox.get("0.0","end")
notes_textbox.pack(padx=20, pady=5)

button = customtkinter.CTkButton(app, text="Save", command=button_callback)
button.pack(padx=20, pady=5)

app.mainloop()
