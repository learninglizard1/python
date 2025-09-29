#### Name: Sachin Bade	
#### Student No. 5117566	
#### BIT502 Assessment 3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3

def show_membership(root):

    root.withdraw() # Hides the main menu
    member_root = tk.Toplevel()
    member_root.title ("Membership Form")
    member_root.geometry ("500x750")

    database_name = ("Records.db")

    membership_prices ={
        "Standard": 10,
        "Premium": 15,
        "Kids": 5
    }

    extras_prices = {
        "Book Rental": 5,
        "Private Area Access": 15,
        "Monthly Booklet":2,
        "Online ebook Rental": 5
    }

    discount = 0.10
    # Functions
    # To insert data into database after a submisison
    def member_submit(First_Name, Last_Name, Address, Mobile, Membership_Plan, Payment_Plan, 
                      Extra_Book_Rental, Extra_Private_Area, Extra_Booklet, Extra_Ebook_Rental, 
                      Has_Library_Card, Library_Card_Number):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Memberships (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    First_Name TEXT,
                    Last_Name TEXT,
                    Address TEXT,
                    Mobile TEXT,
                    Membership_Plan TEXT,
                    Payment_Plan TEXT,
                    Extra_Book_Rental BOOLEAN,
                    Extra_Private_Area BOOLEAN,
                    Extra_Booklet BOOLEAN,
                    Extra_Ebook_Rental BOOLEAN,
                    Has_Library_Card BOOLEAN,
                    Library_Card_Number TEXT
                    )
                """)
        cursor.execute("""
                    INSERT INTO Memberships (
                        First_Name, Last_Name, Address, Mobile, Membership_Plan, Payment_Plan,
                        Extra_Book_Rental, Extra_Private_Area, Extra_Booklet, Extra_Ebook_Rental,
                        Has_Library_Card, Library_Card_Number
                       ) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, (
                        First_Name, Last_Name, Address, Mobile, Membership_Plan, Payment_Plan,
                        Extra_Book_Rental, Extra_Private_Area, Extra_Booklet, Extra_Ebook_Rental,
                        Has_Library_Card, Library_Card_Number
                       ))
        conn.commit()
        cursor.close()

    def submit_form():
        # Get all the values from the form input
        First_Name = fname.get().capitalize()
        Last_Name = lname.get().capitalize()
        Address = address.get()
        Mobile = mobile.get()
        Membership_Plan = mem_plan.get()
        Payment_Plan = pay_plan.get()
        Extra_Book_Rental = book_rental.get()
        Extra_Private_Area = private_area.get()
        Extra_Booklet = booklet.get()
        Extra_Ebook_Rental = ebook_rental.get()
        Has_Library_Card = library_card.get()
        Library_Card_Number = card_number.get()

       
        # Check for required fields  
        # To hide all the errors.
        for error in [error1, error2, error3, error4, error5]:
            error.grid_forget()

        # First name validation
        if not First_Name.isalpha():
            error1.grid(row=2, column=1)
            return
        
        # Last name vvalidation
        if not Last_Name.isalpha():
            error2.grid(row=4, column=1)
            return
        
        # Address validation
        if (len(address.get()) <= 8):
            error3.grid(row=6, column=1)
            return

        # Mobile number validation
        if not Mobile.isdigit():
            error4.grid(row=8, column=1)
            return
        
        if Has_Library_Card:
            if not (Library_Card_Number.isdigit() and len(Library_Card_Number) == 5):
                error5.grid(row =20, column =1) 
                return

        # Calling this function to submit it into the databse
        member_submit(First_Name, Last_Name, Address, Mobile, Membership_Plan, Payment_Plan, 
                      Extra_Book_Rental, Extra_Private_Area, Extra_Booklet, Extra_Ebook_Rental, 
                      Has_Library_Card, Library_Card_Number)
        
        mb.showinfo ("Thank you!", "Membership has been succesffuly submitted.")

        # Clear the membership after completion
        clear_form()
    
    def clear_form():
        mb.showinfo("The Aurora Archive", "Thank you for visiting.")
        # Clearing all the entry fields
        en_fname.delete(0, tk.END)
        en_lname.delete(0, tk.END)
        en_address.delete(0, tk.END)
        en_mobile.delete(0, tk.END)
        en_card_number.delete(0, tk.END)

        # Reset the radio buttons
        mem_plan.set("Standard")
        pay_plan.set("Monthly")

        book_rental.set(False)
        private_area.set(False)
        booklet.set(False)
        ebook_rental.set(False)
        library_card.set(False)

        
        #resetting the values to default which is "--"
        lbl_total_cost_base.config(text= "--")
        lbl_total_cost_extras.config(text= "--")
        lbl_total_weekly_cost.config(text= "--")
        lbl_total_cost_annual.config(text= "--")
        lbl_total_cost_discount.config(text= "--")
        lbl_total_cost_total.config(text= "--")

        
    def calculate(): 
        total = 0
        extras_total = 0
        annual_price = 0

        selected_membership = mem_plan.get()
        selected_payment = pay_plan.get()
        has_card = library_card.get()

        base_price = membership_prices.get(selected_membership, 0)

        # Optional extras
        if book_rental.get():
            extras_total += extras_prices["Book Rental"]
        if private_area.get():
            extras_total += extras_prices["Private Area Access"]
        if booklet.get():
            extras_total += extras_prices["Monthly Booklet"]
        if ebook_rental.get():
            extras_total += extras_prices["Online ebook Rental"]

        monthly_total_before_discounts = base_price + extras_total
        monthly_discount = 0

        # If annual plan is selected
            # Apply discounts
        if selected_payment == "Annual":
            # 1 month free base membership
            annual_base_discount = base_price / 12
            monthly_discount += annual_base_discount

        # Library card discount
        if has_card:
            try:
                library_card.get()
                library_discount = monthly_total_before_discounts * discount
                monthly_discount += library_discount
            except:
                library_discount = 0

        # Final monthly cost
        final_monthly_cost = monthly_total_before_discounts - monthly_discount

        # Weekly cost
        weekly_cost = final_monthly_cost / 4

        # Total and total_discount depending on plan
        if selected_payment == "Annual":
            total = final_monthly_cost * 12
            total_discount = monthly_discount * 12
        else:
            total = final_monthly_cost
            total_discount = monthly_discount

        # Annual price for label display
        annual_price = final_monthly_cost * 12

        # Update GUI labels
        lbl_total_cost_base.config(text=f"${base_price:.2f}")
        lbl_total_cost_extras.config(text=f"${extras_total:.2f}")
        lbl_total_weekly_cost.config(text=f"${weekly_cost:.2f}")
        lbl_total_cost_annual.config(text=f"${annual_price:.2f}" if selected_payment == "Annual" else "--")
        lbl_total_cost_discount.config(text=f"${total_discount:.2f}")
        lbl_total_cost_total.config(text=f"${total:.2f}" + ("/year" if selected_payment == "Annual" else "/month"))
        
    def reset():
        answer = mb.askyesno("The Aurora Archive", "Would you like to reset the form?")
        
        if answer:
             # Clearing all the entry fields
            en_fname.delete(0, tk.END)
            en_lname.delete(0, tk.END)
            en_address.delete(0, tk.END)
            en_mobile.delete(0, tk.END)
            en_card_number.delete(0, tk.END)

            # Reset the radio buttons
            mem_plan.set("Standard")
            pay_plan.set("Monthly")

            book_rental.set(False)
            private_area.set(False)
            booklet.set(False)
            ebook_rental.set(False)
            library_card.set(False)

            
            #resetting the values to default which is "--"
            lbl_total_cost_base.config(text= "--")
            lbl_total_cost_extras.config(text= "--")
            lbl_total_weekly_cost.config(text= "--")
            lbl_total_cost_annual.config(text= "--")
            lbl_total_cost_discount.config(text= "--")
            lbl_total_cost_total.config(text= "--")

            mb.showinfo("Reset", "The form has been reset.")



    # Close the membership form and show us the main screen
    def back():
        answer = mb.askyesno("The Aurora Archive", "Would you like to go back to the Main menu?")

        if answer: 
            member_root.destroy()
            root.deiconify() # Brings back Main menu

    
    # Variables
    fname = tk.StringVar()              # variable to store first name
    lname = tk.StringVar()              # variable to store last nameIntVar
    address = tk.StringVar()            # variable to store address
    mobile = tk.StringVar()             # variable to store mobile number
    mem_plan = tk.StringVar(value = "Standard")        # variable to store membership plan
    pay_plan = tk.StringVar(value="Monthly")           # variable to store payment plan 
    book_rental = tk.BooleanVar()     
    private_area = tk.BooleanVar()
    booklet = tk.BooleanVar()           
    ebook_rental = tk.BooleanVar()      
    library_card = tk.BooleanVar()      
    card_number = tk.StringVar()     


    ############# Widgets ##############

    # Labels
    lbl_field = tk.Label(member_root, text = "Fields with '*' are mandatory.", font= ("Calibri", 12, "bold"), fg= "red")
    lbl_fname = tk.Label(member_root, text="First Name:", font= ("Calibri", 12, "bold"))
    lbl_lname = tk.Label (member_root, text= "Last Name:", font= ("Calibri", 12, "bold"))
    lbl_address = tk.Label (member_root, text="Address:", font= ("Calibri", 12, "bold"))
    lbl_mobile = tk.Label (member_root, text= "Mobile:", font= ("Calibri", 12, "bold"))
    lbl_mem_plan = tk.Label (member_root, text="Membership Plan:", font= ("Calibri", 12, "bold"))
    lbl_pay_plan = tk.Label(member_root, text= "Payment Plan:", font= ("Calibri", 12, "bold"))
    lbl_extras = tk.Label(member_root, text="Extras:", font= ("Calibri", 12, "bold"))
    lbl_library_card = tk.Label(member_root, text="Library Card:", font= ("Calibri", 12, "bold"))
    lbl_cardnumber = tk.Label(member_root, text="Library Card Number:", font= ("Calibri", 12, "bold"))
    
    # Asterisk indicators for mandatory fields
    asterisk1 = tk.Label(member_root, text= "*", fg= "red")
    asterisk2 = tk.Label(member_root, text= "*", fg= "red")
    asterisk3 = tk.Label(member_root, text= "*", fg= "red")
    asterisk4 = tk.Label(member_root, text= "*", fg= "red")
    asterisk5 = tk.Label(member_root, text= "*", fg= "red")


    # Error messages
    error1 = tk.Label (member_root, text="Enter a valid first name.", fg="red")
    error2 = tk.Label (member_root, text= "Enter a valid last name.", fg="red")
    error3 = tk.Label (member_root, text= "Enter a valid address.", fg="red")    
    error4 = tk.Label (member_root, text= "Enter a valid phone number.", fg="red")
    error5 = tk.Label (member_root, text= "Please enter your 5 digits card number.", fg="red")
    
    # Entry forms
    en_fname = tk.Entry(member_root, textvariable = fname, width= 30)
    en_lname = tk.Entry(member_root, textvariable = lname, width= 30)
    en_address = tk.Entry(member_root, textvariable = address, width= 30)
    en_mobile = tk.Entry(member_root, textvariable= mobile, width= 30)
    en_card_number = tk.Entry(member_root, textvariable= card_number, width = 25 )

    # Radio buttons
    rad_standard = tk.Radiobutton(member_root, text= "Standard", variable=mem_plan, value= "Standard", command= calculate)
    rad_premium = tk.Radiobutton(member_root, text="Premium", variable=mem_plan, value= "Premium", command= calculate)
    rad_kids = tk.Radiobutton(member_root, text="Kids", variable= mem_plan, value= "Kids", command= calculate)
    rad_month = tk.Radiobutton(member_root, text="Monthly", variable=pay_plan, value= "Monthly", command= calculate)
    rad_annual = tk.Radiobutton(member_root, text="Annual", variable=pay_plan, value= "Annual", command= calculate)

    # Check buttons
    chk_book = tk.Checkbutton(member_root, text= "Book Rental", variable = book_rental, command= calculate)
    chk_priv = tk.Checkbutton(member_root, text= "Private Area", variable= private_area, command= calculate)
    chk_booklet = tk.Checkbutton(member_root, text= "Booklet", variable= booklet, command= calculate)
    chk_ebook = tk.Checkbutton (member_root, text= "Online Ebook Rental", variable= ebook_rental, command= calculate)
    chk_library_card = tk.Checkbutton(member_root, text="", variable=library_card, command= calculate)

    # Buttons
    sub_btn = tk.Button(member_root, text="Submit", width= 10, command= submit_form, bg= "#14610D", fg= "white")
    memback_btn = tk.Button(member_root, text="Back to main menu", width= 15, command= back)
    reset_btn = tk.Button(member_root, text="Reset", width = 10, command= reset, bg= "#E90F0F")


    # Widget for calculation
    lbl_total_header = tk.Label(member_root, text = "Totals",  font= ("Calibri", 12, "bold"))
    lbl_total_base = tk.Label(member_root, text = "Membership Cost:", font= ("Calibri", 12, "bold"))
    lbl_total_extras = tk.Label(member_root, text = "Extra Charges:", font= ("Calibri", 12, "bold"))
    lbl_total_annual = tk.Label(member_root, text = "Annual Cost:", font= ("Calibri", 12, "bold"))
    lbl_total_discount = tk.Label(member_root, text = "Total Discount:", font= ("Calibri", 12, "bold"))
    lbl_weekly_cost = tk.Label(member_root, text= "Weekly Cost", font= ("Calibri", 12, "bold"))
    lbl_total_final = tk.Label(member_root, text = "Total Cost:", font= ("Calibri", 12, "bold"))


    lbl_total_cost_base = tk.Label(member_root, text = "--")
    lbl_total_cost_extras = tk.Label(member_root, text = "--")
    lbl_total_weekly_cost = tk.Label(member_root, text = "--")
    lbl_total_cost_annual = tk.Label(member_root, text = "--")
    lbl_total_cost_discount = tk.Label(member_root, text = "--")
    lbl_total_cost_total = tk.Label(member_root, text = "--")

    separator = ttk.Separator(member_root, orient= "horizontal")

    # Widget Positions

    lbl_field.grid(row=0, column=1)
    lbl_fname.grid (row=1, column= 0, sticky='w')
    lbl_lname.grid (row=3, column=0, sticky='w')
    lbl_address.grid(row=5, column=0, sticky= 'w')
    lbl_mobile.grid(row=7,column=0, sticky= 'w')
    lbl_mem_plan.grid(row=9, column=0, sticky= 'w')
    lbl_pay_plan.grid(row=12, column= 0, sticky= 'w')
    lbl_extras.grid(row=14, column=0, sticky= 'w')

    en_fname.grid(row=1, column=1)
    en_lname.grid(row=3, column=1)
    en_address.grid(row=5, column=1)
    en_mobile.grid(row=7, column=1)
      
    rad_standard.grid(row= 9, column= 1, sticky='w')
    rad_premium.grid(row= 10, column=1, sticky='w')
    rad_kids.grid(row=11, column=1, sticky='w')    
    rad_month.grid (row=12, column= 1, sticky='w')
    rad_annual.grid(row=13, column=1, sticky='w')

    chk_book.grid(row=14, column=1, sticky= 'sw')
    chk_priv.grid(row=15, column=1, sticky= 'sw')
    chk_booklet.grid(row=16, column=1, sticky= 'sw')
    chk_ebook.grid(row=17, column=1, sticky= 'sw')

    lbl_library_card.grid(row=18, column=0, sticky= 'w')
    chk_library_card.grid(row=18, column=1, sticky='sw')
    lbl_cardnumber.grid(row=19, column=0, sticky='w')
    en_card_number.grid(row=19, column=1)

    asterisk1.grid(row=1, column=1, sticky='ne')
    asterisk2.grid(row=3, column=1, sticky='ne')
    asterisk3.grid(row=5, column=1, sticky='ne')
    asterisk4.grid(row=7, column=1, sticky='ne')
    asterisk5.grid(row=19, column=1, sticky='e')

    lbl_total_header.grid(row = 22, column= 0, pady= (10,5), sticky= 'w')
    lbl_total_base.grid(row=23, column=0, sticky= 'w')
    lbl_total_extras.grid(row=24, column=0, sticky='w')
    lbl_total_annual.grid(row=25, column=0, sticky='w')
    lbl_total_discount.grid(row=26, column=0, sticky='w')
    lbl_weekly_cost.grid(row=27, column=0, sticky='w')
    lbl_total_final.grid(row=28, column=0, sticky='w')

    lbl_total_cost_base.grid(row=23, column=1, sticky='w')
    lbl_total_cost_extras.grid(row=24, column=1, sticky='w')
    lbl_total_cost_annual.grid(row=25, column=1, sticky='w')
    lbl_total_cost_discount.grid(row=26, column=1, sticky='w')
    lbl_total_weekly_cost.grid(row=27, column=1, sticky='w')
    lbl_total_cost_total.grid(row=28, column=1, sticky='w')


    separator.grid(row=21, column= 0, columnspan= 2, sticky='ew', padx=10, pady= 10)

    sub_btn.grid (row=29, column=0, padx= 10, pady= (10,0), sticky= 's')
    memback_btn.grid(row=30, column=1, padx= 10, pady= 10)
    reset_btn.grid(row= 31,column=0, padx= 10)

    member_root.mainloop()
