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
        pad = 3
        self.root.title("Hotel Management System: OceanView")
        self.root.iconbitmap("hms.ico")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
            
        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")
        
        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # display message
        self.label = Label(top, font=('Bookman Old Style', 50, 'bold'), text="Welcome to OceanView!", fg="#330000", anchor="center")
        self.label.grid(row=0, column=3, pady = (0, 30))

        # create check in button
        self.check_in_button = Button(bottom, text="Check In", font=('Bookman Old Style', 20), bg="#330000", relief=RIDGE, height=2, width=50, fg="white", anchor="center", command=check_in_ui.check_in_ui_fun)
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)                              

        # create check out button
        self.check_out_button = Button(bottom, text="Check Out", font=('Bookman Old Style', 20), bg="#330000", relief=RIDGE, height=2, width=50, fg="white", anchor="center", command=check_out.check_out_ui)
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)                                

        # create show list button
        self.room_info_button = Button(bottom, text="Customer Room Info", font=('Bookman Old Style', 20), bg="#330000", relief=RIDGE, height=2, width=50, fg="white", anchor="center", command=get_info.get_info_ui)
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)                              
                                       
        # create get information of all the guest
        self.get_info_button = Button(bottom, text="All Occupants Info", font=('Bookman Old Style', 20), bg="#330000", relief=RIDGE, height=2, width=50, fg="white", anchor="center", command=customer_info.customer_info_ui)
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)                              
                                      
        # button to exit the program
        self.exit_button = Button(bottom, text="Exit", font=('Bookman Old Style', 20), bg="#000000", relief=RIDGE, height=1, width=30, fg="white", anchor="center", command=quit)
        self.exit_button.grid(row=4, column=2, padx=10, pady=10)

        # button to view the about page
        self.about_button = Button(bottom, text = 'about', font = ('Bookman Old Style', 15), bg = '#450000', relief=RIDGE, height=1, width=30, fg="white", anchor="center", command=about.about_ui)
        self.about_button.grid(row = 5, column = 2, padx = 10, pady = 10)


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()                                      