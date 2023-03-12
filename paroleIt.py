import random
from tkinter import *
import tkinter.messagebox

# Creating main class
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

# Configure widgets module
    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Choose a length of your new password")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

# Text field
        self.pwlen_ent = Entry(self, width = 5)
        self.pwlen_ent.grid(row = 0, column = 2, sticky = E)

# Button
        self.submit_bttn = Button(self, text = "Generate new password", command = self.reveal)
        self.submit_bttn.grid(row = 1, column = 0, sticky = W)

# Text field for generated password

        self.pw_gentd = Entry(self, width = 0)
        self.pw_gentd.grid(row = 2, column = 0, sticky = W)

# Reveal module
    def reveal(self):
        try:
            contents = int(self.pwlen_ent.get())
        except:
            tkinter.messagebox.showinfo("Error", "You need enter a number")

        if contents < 10:
            message = "Your password will be too easy. Try again"
        elif contents > 15:
            message = "Not necessary to set up such long password. Try again"
        else:
            password_length = 0
            symbols = ""
            while password_length != contents:
                new_password = random.randrange(33, 127)
                new_password = chr(new_password)
                symbols += new_password
                password_length += 1
            message = symbols

        self.pw_gentd.delete(0, END)
        self.pw_gentd.insert(0, message)

# Main
root = Tk()
root.title("Parole It")
app = Application(root)
root.mainloop()