import tkinter as tk
from PIL import ImageTk

bg_colour = "#3d6466"

# initiallize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame1.grid(row=0, column=0)
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

# run app
root.mainloop()
