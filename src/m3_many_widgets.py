import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Window")
window.configure(cursor = "heart")

frm_1 = tk.Frame(
    window,
    bg = "#FFC0CB",
    width = 30, 
    height = 10
)
frm_1.configure(
    borderwidth = 5, 
    relief = 'raised'
)
frm_1.pack_propagate()
frm_1.pack(padx = 20, pady = 20, ipady = 5, ipadx = 5, side = "left")

lbl_1 = tk.Label(
    frm_1,
    text = "1st Frame",
    font = "Times 20 italic bold",
    bg = "#F88379",
    fg = "#770737",
    width = 20, 
    height = 3,
    relief = "ridge"
)
lbl_1.pack(padx = 5, pady = 5)

button = tk.Button(
    frm_1,
    text = "Button Doing Button Things",
    font = "Times 9 underline bold",
    fg = "#E0115F",
    bg = "#F3CFC6"
)
button.pack(padx = 5, pady = 5)

single_line_entry = tk.Entry(
    frm_1,
    font = "Times 15 italic",
    width = 30,
    relief = "groove",
    bg = "#FAA0A0",
    fg = "#811331",
    borderwidth = 3
)
single_line_entry.pack(pady = 5)

single_line_entry.insert(0,"You cannot type a lot here :(")

frm_2 = tk.Frame(
    window,
    bg = "#FAA0A0",
    width = 30, 
    height = 10
)
frm_2.configure(
    borderwidth = 5, 
    relief = 'sunken'
)
frm_2.pack_propagate()
frm_2.pack(padx = 20, pady = 20, ipady = 5, ipadx = 5, side = "right")

lbl_2 = tk.Label(
    frm_2,
    text = "2nd Frame",
    font = "Times 20 italic bold",
    bg = "#E0115F",
    fg = "#F88379",
    width = 20, 
    height = 3,
    relief = "ridge"
)
lbl_2.pack(padx = 5, pady = 5)

scroller = tk.Scrollbar(
    frm_2,
    orient = "vertical",
    bg = "#770737"
)
scroller.pack(side = "right", fill = "y")

text_box = tk.Text(
    frm_2,
    width = 30,
    height = 3,
    font = "Times 15 italic",
    relief = "groove",
    bg = "#811331",
    fg = "#F3CFC6",
    borderwidth = 3,
    yscrollcommand = scroller.set
)
text_box.insert("1.0","You can type a lot here! ;)\n\n\n\n\n\n\n\n\n\n")
text_box.insert("10.0","You can see me if you use the bar!")

scroller.configure(command = text_box.yview)
text_box.pack()

window.mainloop()

