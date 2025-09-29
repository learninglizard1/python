#### Name: Sachin Bade	
#### Student No. 5117566	
#### BIT502 Assessment 3

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


def show_search(root):
    root.withdraw() # Hides Main menu
    search_root = tk.Toplevel()
    search_root.title ("Search")
    search_root.geometry ("1040x520")

    database_name = "Records.db"
    table_name = "Memberships"

    #################################
    # Database functions

    def select_query(query):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    ##################################
    # 


    def submit():

        # Query part
        query = f"SELECT * FROM {table_name} "    

        query_parts = []
        if(partial.get()):
            if(edit_fname.get()):
                query_parts.append(f"(First_Name LIKE '%{edit_fname.get()}%')")
            if(edit_lname.get()):
                query_parts.append(f"(Last_Name LIKE '%{edit_lname.get()}%')")
            if(edit_membership.get()):
                query_parts.append(f"(Membership_Plan LIKE '%{edit_membership.get()}%')")
        else:
            if(edit_fname.get()):
                query_parts.append(f"(First_Name = '{edit_fname.get()}')")
            if(edit_lname.get()):
                query_parts.append(f"(Last_Name = '{edit_lname.get()}')")
            if(edit_membership.get()):
                query_parts.append(f"(Membership_Plan = '{edit_membership.get()}')")

        
        # For payment plan we only need to check if they've selected an option
        if(payment_var.get() == 1):
            query_parts.append("(Payment_Plan = 'Monthly')")
        elif (payment_var.get() == 2):
            query_parts.append("(Payment_Plan = 'Annual')")


        # If at least one query is entered, we need to add WHERE to the query
        if(len(query_parts)):
            query += "WHERE "

        # Combine the query parts into the main query
        for i in range(len(query_parts)):
            part = query_parts[i]
            query += part                       # Add the part to the string
            if(not i == len(query_parts)-1):      # If we are NOT on the last in the list
                # We need to add AND after each part, EXCEPT the last one added
                query += " AND"

        # Finish off the query
        # Collate if an option was selected
        if(len(query_parts)):
            query += " COLLATE NOCASE"

        # If a query has been built, you could do additional validation too
        if(query):      
            rows = select_query(query)      # Run our query to get rows
            update_treeview(rows)           # Update the treeview with our rows

        

    def back():
        search_root.destroy()
        root.deiconify() # Brings back main menu


    # Variable names

    edit_fname = tk.StringVar()
    edit_lname = tk.StringVar()
    edit_membership = tk.StringVar()
    partial = tk.IntVar()
    payment_var = tk.IntVar()

    search_frame = tk.LabelFrame(search_root, text="Search Options")

    lbl_fname = ttk.Label(search_frame, text= f"First Name:")
    lbl_lname = ttk.Label(search_frame, text= f"Last Name:")
    lbl_membership = ttk.Label(search_frame, text= f"Membership Plan:")
    lbl_payment = ttk.Label(search_frame, text= f"Payment Plan:")


    en_fname = ttk.Entry(search_frame, textvariable=edit_fname)
    en_lname = ttk.Entry(search_frame, textvariable=edit_lname)
    en_membership = ttk.Entry(search_frame, textvariable= edit_membership)

    rad_button1 = ttk.Radiobutton(search_frame, text= "Monthly", variable= payment_var, value= 1)
    rad_button2 = ttk.Radiobutton(search_frame, text="Annual", variable= payment_var, value= 2)
    rad_button3 = ttk.Radiobutton(search_frame, text = "Either", variable= payment_var, value= 3)

    button = ttk.Button (search_frame, text="Submit", command= submit)
    partial_button = ttk.Checkbutton (search_frame, text= "Partial Match", variable= partial)


    # Widget Positions
    lbl_fname.grid (row=0, column=0, sticky= 'w')
    en_fname.grid(row=0, column=1)

    lbl_lname.grid(row=1, column=0, sticky= 'w')
    en_lname.grid(row=1, column=1)

    lbl_membership.grid(row=2, column=0, sticky= 'w')
    en_membership.grid(row=2, column=1)

    partial_button.grid(row=3, column=1, sticky= 'w')
    button.grid(row=4, column=1, columnspan=2, sticky= 'w')

    lbl_payment.grid(row=0, column=2, padx=(40, 0), sticky='nw')
    rad_button1.grid(row=1, column=2, padx= (40, 0), sticky='w')
    rad_button2.grid(row=2, column=2, padx= (40, 0), sticky='w')
    rad_button3.grid(row=3, column=2, padx= (40, 0), sticky='w')



    #############################################
    # treeview code

    tree_frame = tk.LabelFrame(search_root, text= "Search Results")

    tree = ttk.Treeview (tree_frame, columns=["ID", "First Name", "Last Name", "Membership Plan", "Payment Plan"], show= "headings")

    def update_treeview(rows):
        temp_list = []

        if not rows:
            mb.showinfo("The Aurora Archive", "No results found.")
            return
        
        for member in rows:
            temp_list.append((member[0], member[1], member[2], member[5], member[6]))

        for row in temp_list:
            tree.insert("", tk.END, values = row)

        if temp_list == "":
            answer = mb.askretrycancel("The Aurora Archive", "No results found.")
            if answer:
                return
            
    def clear():
        for item in tree.get_children():
            tree.delete(item)

        edit_fname.set("")
        edit_lname.set("")
        edit_membership.set("")
        partial.set(0)
        payment_var.set(0)

    tree.heading ("ID", text="ID")
    tree.heading ("First Name", text="First Name")
    tree.heading ("Last Name", text="Last Name")
    tree.heading ("Membership Plan", text="Membership Plan")
    tree.heading ("Payment Plan", text= "Payment Plan")

    tree.grid(row=0, column=0, sticky="nsew")
    # END Treeview code

    # Position the frames
    scrollbar = ttk.Scrollbar(tree_frame, orient= tk.VERTICAL, command = tree.yview)
    tree.configure (yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky= 'ns')


    search_frame.grid(row=0, column=0,  padx=20, pady=20, sticky="ew")
    tree_frame.grid( row=1, column=0, padx=20, pady=20, sticky="we")

    # Button

    # Clear the search form
    clear_btn = tk.Button (search_root, text = "Clear search", width= 10, command= clear)
    clear_btn.grid(row=2, column=0, pady= 5)
    
    # Go back to main menu
    back_btn = tk.Button (search_root, text="Back to Main menu", command = back)
    back_btn.grid(row= 3, column=0)



    search_root.mainloop()
