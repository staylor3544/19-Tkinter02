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
# DONE: 2. (2 pts)
#
#   Now, create a multiline text entry box called text_box.
#
#   Make sure you use the textbox's pack() method to add it to your window.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
# DONE: 3. (2 pts)
#
#   Now, use the insert() method to insert text into the multiline text box.
#   You can choose the text that you insert, but you should insert text on
#   multiple lines.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
# DONE: 4. (2 pts)
#
#   Now, use the get() method to get the text that you inserted. Save that
#   text to a variable and then print that variable.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
# DONE: 5. (1 pt)
#
#   Now, use the delete() method to delete only the first line of text
#   (leaving the first line as a blank line).
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Window")

text_box = tk.Text(
    window,
    font = "Times 10 italic"
)
text_box.pack()

text_box.insert("1.0","This is line one")
text_box.insert("2.0", "\nThis is line two")
text_box.insert(tk.END,"\nThis is at at the end:)")

my_text = text_box.get("1.0", tk.END)
print(my_text)

text_box.delete("1.0", "1.17")

window.mainloop()