from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info
import about
import os

class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Remove window decorations (title bar, borders)
        self.root.attributes("-alpha", 1.0)  # Set window transparency to 1.0 (fully opaque)
        self.root.iconbitmap("hms.ico")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        
        # Create a main frame to add a welcome message
        top = Frame(self.root)
        top.pack(side="top", pady=30)

        # Create a frame to add buttons
        bottom = Frame(self.root, bg="white")
        bottom.pack(side="top", pady=20)

        # Display a welcome message
        self.label = Label(top, font=('Bookman Old Style', 50, 'bold'), text="Welcome to OceanView!", fg="#330000", anchor="center", bg="white")
        self.label.grid(row=0, column=0, columnspan=6)  # Set columnspan to match the number of buttons

        # Create buttons and customize their appearance with larger size
        button_size = (20, 3)  # Button size (width, height)
        button_font_size = 16
        buttons = [
            {"text": "Check In", "command": check_in_ui.check_in_ui_fun},
            {"text": "Check Out", "command": check_out.check_out_ui},
            {"text": "Customer Room Info", "command": get_info.get_info_ui},
            {"text": "All Occupants Info", "command": customer_info.customer_info_ui},
            {"text": "Exit", "command": quit},
            {"text": "About", "command": about.about_ui}
        ]

        for i, button_info in enumerate(buttons):
            button = Button(bottom, text=button_info["text"], font=('Bookman Old Style', button_font_size), bg="#330000", relief=RIDGE, width=button_size[0], height=button_size[1], fg="white", anchor="center", command=button_info["command"])
            button.grid(row=0, column=i, padx=10, pady=10, sticky='nsew')

        # Ensure that buttons expand within their grid cell to fill the cell properly
        bottom.grid_rowconfigure(0, weight=1)  
        for i in range(6):
            bottom.grid_columnconfigure(i, weight=1)  # Ensure buttons expand in the x-axis

    

def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()

if __name__ == '__main__':
    home_ui()                                