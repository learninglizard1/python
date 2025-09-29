#### Name: Sachin Bade	
#### Student No. 5117566	
#### BIT502 Assessment 3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


def show_help(root):
    
    root.withdraw() # Hides the main menu
    help_root = tk.Toplevel(root)
    help_root.title("Help")
    help_root.resizable(False, False)
    
    # Membership cost
    standard_cost = 10
    premium_cost = 15
    kids_cost = 5

    # Extras cost
    book_rental_cost = 5
    private_area_cost = 15
    monthly_book_cost = 2
    online_book_cost = 5

    def more():
        lbl_standard.grid(row= 2 , column= 0, columnspan= 2, sticky= 'w',padx= 10)
        lbl_premium.grid(row= 3 , column= 0, columnspan= 2, sticky= 'w',padx= 10)
        lbl_kids.grid(row= 4 , column= 0, columnspan= 2, sticky= 'w',padx= 10)
        lbl_book.grid(row= 5 , column= 0, columnspan= 2, sticky= 'w',padx= 10)
        lbl_private.grid(row= 6 , column= 0, columnspan= 2, sticky= 'w',padx= 10)
        lbl_booklet.grid(row= 7 , column= 0, columnspan= 2, sticky= 'w',padx= 10)
        lbl_ebook.grid(row= 8 , column= 0, columnspan= 2, sticky= 'w',padx= 10)
        
        btn_more.config(state="disabled")

    def back():
        help_root.destroy()
        root.deiconify() # Brings back Mainmenu

    # Widgets 
    lbl_help1 = ttk.Label(help_root, text= "About this program\nVersion 1.0\nThe Aurora Archive book established 2020.")
    btn_ok = ttk.Button(help_root, text="Ok", command= back)
    btn_more = ttk.Button(help_root, text="Pricing Details...", command= more)
    
    # Widget positions
    lbl_help1.grid (row= 0, column=0, padx= 2, pady= 2)

    lbl_standard= ttk.Label(help_root, text= f"Standard : ${standard_cost}" )
    lbl_premium = ttk.Label(help_root, text= f"Premium : ${premium_cost}")   
    lbl_kids = ttk.Label(help_root, text= f"Kids: ${kids_cost}")
    lbl_book = ttk.Label(help_root, text= f"Book Rental: ${book_rental_cost}")
    lbl_private = ttk.Label(help_root, text= f"Private Area: ${private_area_cost}")
    lbl_booklet = ttk.Label(help_root, text= f"Monthly Booklet: ${monthly_book_cost}")
    lbl_ebook = ttk.Label(help_root, text= f"Online Ebook Rental: ${online_book_cost}")

    btn_more.grid(row=1, column=0, sticky= 'w', padx= 5, pady= 5)
    btn_ok.grid(row=1, column=1, padx= 5, pady= 5)
    
    