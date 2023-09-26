import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random

bg_colour = "#3d6466"


def fetch_db():
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table'; ")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables) - 1)

    # fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_name, table_records


def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])
    print(title)


def load_frame1():
    frame1.pack_propagate(False)
    # frame1 widgets
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

    # text
    tk.Label(
        frame1,
        text="ready for your random recipe?",
        bg=bg_colour,
        fg="white",
        font=("TkMenuFont", 14),
    ).pack()

    # frame1 button
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame2(),
    ).pack(pady=20)


def load_frame2():
    table_name, table_records = fetch_db()
    pre_process(table_name, table_records)


# initiallize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()


# run app
root.mainloop()
