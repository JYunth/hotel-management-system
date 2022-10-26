import sqlite3
from tkinter import *
import main


class CheckOut:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Check out of OceanView")
        self.root.iconbitmap("hms.ico")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        bottom = Frame(self.root)
        bottom.pack(side="top")

        info_frame = Frame(self.root)
        info_frame.pack(side="top")   

        # display message
        self.label = Label(top, font=('Bookman Old Style', 50, 'bold'), text="Check out of Oceanview", fg="#330000", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)
        
        #room number
        self.room_no_label = Label(bottom, font=('Bookman Old Style', 20, 'bold'), text="Enter Room Number: ", fg="#330000", anchor="center")
        self.room_no_label.grid(row=2, column=2, padx=10, pady=(70, 10))                           
        
        # text entry field for room number
        self.room_var = IntVar()
        self.room_no_entry = Entry(bottom, width=5, text=self.room_var, font="14")
        self.room_no_entry.grid(row=2, column=3, padx=10, pady=(70, 10))

        # info window
        self.get_info_entry = Text(info_frame, height=15, width=90)
        self.get_info_entry.grid(row=1, column=1, padx=10, pady=10)


        def check_out():
            room_number1 = int(self.room_no_entry.get())
            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT,Address TEXT,mobile_number TEXT,number_days TEXT,'
                'room_number NUMBER)')
            conn.commit()
            with conn:
                cursor.execute("SELECT room_number FROM Hotel")
                ans = cursor.fetchall()
                room = []
                for i in ans:
                    room.append(i[0])
                if room_number1 in room:
                    with conn:
                        cursor.execute("SELECT Fullname,room_number FROM Hotel")
                        ans = cursor.fetchall()
                        for i in ans:
                            if room_number1 == int(i[1]):
                                self.get_info_entry.insert(INSERT, '\n' + str(i[0]) + ' has successfully checked out from OceanView room number: ' + str(i[1]) + '\n')
                                                           
                                with conn:
                                    cursor.execute("""DELETE FROM Hotel where room_number = ?""", [room_number1])

                else:
                    self.get_info_entry.insert(INSERT, "Please enter valid room number!")

        # create submit button
        self.check_out_button = Button(bottom, text="Check out", font=('Bookman Old Style', 15), bg="#330000", relief=RIDGE, height=2, width=15, fg="white", anchor="center", command=check_out)
        self.check_out_button.grid(row=3, column=2, padx=10, pady=(10, 20))                               
                                       
        # create home button
        self.home_button = Button(bottom, text="Home", font=('Bookman Old Style', 15), bg="#330000", relief=RIDGE, height=2, width=15, fg="white", anchor="center", command=self.root.destroy)
        self.home_button.grid(row=3, column=3, padx=10, pady=(10, 20))                          
        

def check_out_ui():
    root = Tk()
    application = CheckOut(root)
    root.mainloop()