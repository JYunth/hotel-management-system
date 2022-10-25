from tkinter import *
import main

class About:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("About the program")
        self.root.iconbitmap("hms.ico")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        self.top = Frame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")

        self.info_frame = Frame(self.root)
        self.info_frame.pack(side="top")

        

        #title
        self.About = Label(self.top, font=('Bookman Old Style', 50, 'bold'), text = "About the program:", fg = '#330000', anchor = 'center')
        self.About.grid(row = 0, column = 0, columnspan = 2)

        #Description
        self.desc1 = Label(self.top, font = ('Bookman Old Style', 20), text = 'HMS is a program that keeps track of all your occupants, 24/7.', fg = '#330000', anchor = 'w')
        self.desc2 = Label(self.top, font = ("Bookman Old Style", 20), text = 'With SQLite integration, all your information is stored in a ', fg = '#330000', anchor = 'w')
        self.desc3 = Label(self.top, font = ("Bookman Old Style", 20), text= 'SQLite database file (.db), so your information is not lost when you close the program.', fg = '#330000', anchor = 'w')
        self.desc4 = Label(self.top, font = ("Bookman Old Style", 20), text = 'Seamlessly keep track of check-ins and check-outs from your hotel.', fg = '#330000', anchor = 'w')
        self.desc5 = Label(self.top, font = ("Bookman Old Style", 20), text = 'View all your occupants, the room they occupy and their details with just one click.', fg = '#330000', anchor = 'w')
        self.desc6 = Label(self.top, font = ("Bookman Old Style", 20), text = 'Light, fast and resourceful. The perfect companion for the urban hotel owner.', fg = '#330000', anchor = 'w')
    
        
        self.desc1.grid(row = 1, column = 0, columnspan = 2, pady = 10)
        self.desc2.grid(row = 2, column = 0, columnspan = 2)
        self.desc3.grid(row = 3, column = 0, columnspan = 2, pady = (0, 10))
        self.desc4.grid(row = 4, column = 0, columnspan = 2, pady = (0, 10))
        self.desc5.grid(row = 5, column = 0, columnspan = 2, pady = (0, 10))
        self.desc6.grid(row = 6, column = 0, columnspan = 2, pady = (0, 10))

        #This program was made by:
        self.line1 = Label(self.top, font = ('Bookman Old Style', 30, 'bold'), text = "This program was made by: ", fg = '#330000', anchor = 'w')
        self.line1.grid(row = 7, column = 0, columnspan =  2, pady = (0, 15))

        #Jheyanth
        self.jhey = Label(self.top, font = ('Bookman Old Style', 20), text = "CS Jheyanth", fg = '#330000', anchor = 'w')
        self.jhey.grid(row = 8, column = 0, pady = (0,10))

        #Abhishek A
        self.abhi = Label(self.top, font = ('Bookman Old Style', 20,), text = "A Abhishek", fg = '#330000', anchor = 'w')
        self.abhi.grid(row = 9, column = 0)

        #P Pazhaniyappan
        self.paz = Label(self.top, font = ('Bookman Old Style', 20), text = 'P Pazhaniyappan', fg = '#330000', anchor = 'w')
        self.paz.grid(row = 8, column = 1, pady = (0,10))

        #Nikhil Mishra
        self.nikhil = Label(self.top, font = ('Bookman Old Style', 20), text = 'Nikhil Mishra', fg = '#330000', anchor = 'w')
        self.nikhil.grid(row = 9, column = 1)

        # back to home page
        self.back_home_button = Button(self.info_frame, text="Home", font=('Bookman Old Style', 15), bg="#330000", relief=RIDGE, height=2, width=15, fg="white", anchor="center", command=self.root.destroy)                               
        self.back_home_button.grid(row=10, column=0, padx=10, pady=10, columnspan = 2)



def about_ui():
    root = Tk()
    application = About(root)
    root.mainloop()

