#### Name: Sachin Bade	
#### Student No. 5117566	
#### BIT502 Assessment 3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3



def show_statistics(root):
    
    root.withdraw() # Hides the main menu
    statistics_root = tk.Toplevel()
    statistics_root.title ("Statistics")
    statistics_root.geometry("900x540")

    database_name = "Records.db"
    table_name = "Memberships"

    # Database functions

    def total():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        cursor.close()
        return count


    def standard():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Membership_Plan = 'Standard'")
        count = cursor.fetchone()[0]
        cursor.close()
        return count
    
    def premium():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Membership_Plan = 'Premium'")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def kids():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Membership_Plan = 'Kids'")
        count = cursor.fetchone()[0]
        cursor.close()
        return count
    
    def monthly():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Payment_Plan = 'Monthly'")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def annual():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Payment_Plan = 'Annual'")
        count = cursor.fetchone()[0]
        cursor.close()
        return count
    
    def book_rental():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Extra_Book_Rental = 1")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def private_area():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Extra_Private_Area = 1")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def monthly_booklet():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Extra_Booklet = 1")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def online_ebook():
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE Extra_Ebook_Rental = 1")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def back():
        statistics_root.destroy()
        root.deiconify()

    # Widgets and frame 

    stat_frame = tk.LabelFrame(statistics_root, text= "Stats")

    lbl_total = ttk.Label(stat_frame, text= "Total number of members:")
    lbl_monthly = ttk.Label( stat_frame, text= "No. of members in monthly subscription:")
    lbl_annual = ttk.Label(stat_frame,text= "No. of members in annual subscription:")

    label_total = ttk.Label(stat_frame, text="--")
    label_total.config(text=total())
    label_monthly = ttk.Label(stat_frame, text = "--")
    label_monthly.config(text=monthly())
    label_annual = ttk.Label(stat_frame, text= "--")
    label_annual.config(text=annual())

    

    

    # Widget positions 
    stat_frame.grid(row=0, column=0, padx= 20, pady=20, sticky='we')

    lbl_total.grid (row=1, column=0, sticky='w')
    label_total.grid (row=1, column=1, sticky='w', padx=(10, 80))

    lbl_monthly.grid(row=2, column=0, sticky='w')
    label_monthly.grid(row=2, column=1, sticky='w', padx=(10, 80))

    lbl_annual.grid(row=3, column=0, sticky='w')
    label_annual.grid(row=3, column=1, sticky='w', padx= (10, 0))

    


    ###################### VARIABLES ##########################    
    # Membership cost
    standard_cost = 10
    premium_cost = 15
    kids_cost = 5

    # Extras cost
    book_rental_cost = 5
    private_area_cost = 15
    monthly_book_cost = 2
    online_book_cost = 5
    


    # Variable for each member count for different variations
    standard_count = standard()
    total_standard = standard_cost * standard_count

    premium_count = premium()
    total_premium = premium_cost * premium_count

    kids_count = kids()
    total_kids = kids_cost * kids_count

    book_rental_count = book_rental()
    total_book_rental = book_rental_cost * book_rental_count

    private_area_count = private_area()
    total_private_area = private_area_cost * private_area_count

    booklet_count = monthly_booklet()
    total_booklet = monthly_book_cost * booklet_count

    online_ebook_count = online_ebook()
    total_online_ebook =  online_book_cost * online_ebook_count 
    
    tree_frame = tk.LabelFrame(statistics_root, text= "Statistics" )

    tree = ttk.Treeview(tree_frame, columns= ["Option", "Cost Per Unit", "Member Amount", "Total Income"], show= "headings")

    tree.heading ("Option", text= "Option")
    tree.heading ("Cost Per Unit", text= "Cost Per Unit")
    tree.heading ("Member Amount", text= "Member Amount")
    tree.heading ("Total Income", text= "Total Income")

    tree.insert("", "end", values= ("Standard Plan", f"{standard_cost}", f"{standard_count}", f"{total_standard}"))
    tree.insert ("", "end", values= ("Premium Plan", f"{premium_cost}", f"{premium_count}", f"{total_premium}"))
    tree.insert("", "end", values= ("Kids Plan", f"{kids_cost}", f"{kids_count}", f"{total_kids}"))
    tree.insert("", "end", values= ("Book Rental", f"{book_rental_cost}", f"{book_rental_count}", f"{total_book_rental}"))
    tree.insert("", "end", values= ("Private Area Access", f"{private_area_cost}", f"{private_area_count}", f"{total_private_area}"))
    tree.insert("", "end", values= ("Monthly Booklet", f"{monthly_book_cost}", f"{booklet_count}", f"{total_booklet}"))
    tree.insert("", "end", values= ("Online Ebook Rental", f"{online_book_cost}", f"{online_ebook_count}", f"{total_online_ebook}"))

    tree.grid(row=0, column=0, sticky= 'nsew')
    tree_frame.grid(row = 1, column=0, padx=20, pady=20, sticky='ew')

    # back button
    back_btn = tk.Button(statistics_root, text="Back to Main menu", command = back)
    back_btn.grid(row= 3, column=0)

    statistics_root.mainloop()