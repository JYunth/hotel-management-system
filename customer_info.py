import sqlite3
from tkinter import *
import main


class CustomerInfo:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Customer Info")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
            

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        left = Frame(self.root, relief="solid")
        left.pack(side="left")

        right = Frame(self.root, relief="solid")
        right.pack(side="left")

        # display title
        self.label = Label(top, font=('Bookman Old Style', 50, 'bold'), text="Customer List", fg="#330000", anchor="center")
        self.label.grid(row=0, column=0, padx=10, pady=(10, 70), columnspan=2)

        #name
        self.name_label = Label(left, font=('Bookman Old Style', 20, 'bold'), text="Names of Occupants:", fg="#330000", anchor="center")
        self.name_label.grid(row=1, column=0, padx=10, pady=10)

        # textinfo field for names
        self.name_customer_entry = Text(left, height=30, width=70)
        self.name_customer_entry.grid(row=2, column=0, padx=10, pady=10)

        #room number
        self.room_no_label = Label(right, font=('Bookman Old Style', 20, 'bold'), text="Room Number of occupant:", fg="#330000", anchor="center")
        self.room_no_label.grid(row=1, column=1, padx=10, pady=10)

        # textinfo field for room numbers
        self.room_no_customer_entry = Text(right, height=30, width=70)
        self.room_no_customer_entry.grid(row=2, column=1, padx=10, pady=10)

        # create home button
        self.home_button = Button(top, text="Home", font=('Bookman Old Style', 15), bg="#330000", relief=RIDGE, height=2, width=15, fg="white", anchor="center", command=main.home_ui)
        self.home_button.grid(row=1, column=0, padx=10, pady=10)                          
        

        def display_info():

            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT,Address TEXT,mobile_number TEXT,number_days TEXT,'
                'room_number NUMBER)')
            conn.commit()
            with conn:
                cursor.execute("SELECT Fullname FROM Hotel")
                ans = cursor.fetchall()
                for i in ans:
                    self.name_customer_entry.insert(INSERT, i[0] + '\n')

            with conn:
                cursor.execute("SELECT room_number FROM Hotel")
                ans = cursor.fetchall()
                for i in ans:
                    self.room_no_customer_entry.insert(INSERT, str(i[0]) + '\n')


        # create display button
        self.display_button = Button(top, text="Display Results", font=('Bookman Old Style', 15), bg="#330000", relief=RIDGE, height=2, width=15, fg="white", anchor="center", command=display_info)
        self.display_button.grid(row=1, column=1, padx=10, pady=10)                             
        
        
def customer_info_ui():
    root = Tk()
    application = CustomerInfo(root)
    root.mainloop()
