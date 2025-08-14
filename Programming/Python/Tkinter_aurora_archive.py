
# _____________________________----
# Imports
# _____________________________----
import tkinter
from tkinter import messagebox

# _____________________________----
# Tkinter setup
# _____________________________----

window = tkinter.Tk()
window.title("The Aurora Archive")

# _____________________________----
# Variables
# _____________________________----

plan_standard = "Standard"
plan_premium = "Premium"
plan_kids = "Kids"

plan_monthly = "Monthly"
plan_annual = "Annual"

optional_1 = "Book Rental"
optional_2 = "Private Area Access"
optional_3 = "Monthly Booklet"
optional_4 = "Online ebook Rental"

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

# Variables that store the results of the elements

membership_plan = tkinter.StringVar(window, plan_standard)      # Selected membership type
payment_plan = tkinter.StringVar(window, plan_monthly)          # Duration of payment
extra1 = tkinter.BooleanVar(window, False)                      # Optional extra 1
extra2 = tkinter.BooleanVar(window, False)                      # Optional extra 2
extra3 = tkinter.BooleanVar(window, False)                      # Optional extra 3
extra4 = tkinter.BooleanVar(window, False)                      # Optional extra 4
has_library_card = tkinter.BooleanVar(window, False)            # Library Card


# _____________________________----
# Functions
# _____________________________----

#calculate function
def calculate(): 
    total = 0
    extras_total = 0
    annual_price = 0

    selected_membership = membership_plan.get()
    selected_payment = payment_plan.get()
    has_card = has_library_card.get()

    base_price = membership_prices.get(selected_membership, 0)

    # Optional extras
    if extra1.get():
        extras_total += extras_prices["Book Rental"]
    if extra2.get():
        extras_total += extras_prices["Private Area Access"]
    if extra3.get():
        extras_total += extras_prices["Monthly Booklet"]
    if extra4.get():
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
            entry_library_number.get()
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
    label_total_cost_base.config(text=f"${base_price:.2f}")
    label_total_cost_extras.config(text=f"${extras_total:.2f}")
    label_total_weekly_cost.config(text=f"${weekly_cost:.2f}")
    label_total_cost_annual.config(text=f"${annual_price:.2f}" if selected_payment == "Annual" else "--")
    label_total_cost_discount.config(text=f"${total_discount:.2f}")
    label_total_cost_total.config(text=f"${total:.2f}" + ("/year" if selected_payment == "Annual" else "/month"))

    return total, extras_total, base_price, weekly_cost, total_discount #returning variables to use them in other functions



#subtmit function
def submit():
    total, extras_total, base_price, weekly_cost, total_discount = calculate()  #calling variables from a different function

    #collect user inputs#
    #checking first name entries
    first_name = entry_first_name.get().strip().capitalize()
    if first_name == "":
        print ("Please enter your first name.")
        return
    if not first_name.isalpha():
        print ("Invalid characters. Please enter your first name only using alphabets.")
        return 
    
    #checking last name entries
    last_name = entry_last_name.get().strip().capitalize()
    if last_name == "":
        print("Please enter your last name.")
        return
    if not last_name.isalpha():
        print ("Invalid characters. Please enter your last name only using alphabets.")
        return

    #checking address entries
    address = entry_address.get()
    if address == "":
        print(" Please enter your address.")
        return
    if len(address) < 10: 
        print ("Address name too short. Please try again.")
        return

    #checking mobile number entries
    mobile = entry_mobile.get()
    if mobile == "":
        print ("Please enter your phone number")
        return
    if not mobile.isdigit():
        print ("Incorrect phone number. Only numbers are allowed.")
        return
    

    #naming variables for writing
    membership = membership_plan.get()
    payment = payment_plan.get()

    library_card_number = entry_library_number.get() 
    library_card = has_library_card.get()
    if library_card:
        card_number = entry_library_number.get()
        if len(card_number) == 5 and card_number.isdigit():
            print("Thank you! you have been verified.")
        else:
            print("Invalid card number. Please enter your 5-digit card number.")
            return
        

    answer = messagebox.askyesno("The Aurora Archive", "Would you like to submit your form?")
    if answer:
        messagebox.showinfo("The Aurora Archive","Information has been saved.")

        #writing file in members_data.txt to save information
        file_path = ".\\members_data.txt"

        try:
            with open (file_path, "a") as f:
                f.write (f"First name: {first_name}\n")
                f.write (f"Last name: {last_name}\n")
                f.write (f"Address: {address}\n")
                f.write (f"Mobile: {mobile}\n")
                f.write (f"Membership type: {membership}\n")

                #Only the selected check boxes will be written 
                selected_extras = []
                if extra1.get():
                    selected_extras.append("Book Rental")
                if extra2.get():
                    selected_extras.append("Private Area Access")
                if extra3.get():
                    selected_extras.append("Monthly Booklet")
                if extra4.get():
                    selected_extras.append("Online ebook Rental")

                if selected_extras:
                    f.write("Extras: ")
                    for extra in selected_extras:
                        f.write(f"{extra}, ")
                else:
                    f.write("Extras: None")
                f.write (f"\nPayment Plan: {payment}\n")
                f.write (f"Library Card: {library_card}\n")

                #adding if/else statement to add library card number only after user checks
                if library_card == True:
                    f.write (f"Library Card Number: {library_card_number}\n" )
                else:
                    f.write (f"Library Card Number: None\n" )
                f.write (f"\n")
                f.write (f"\n")
                f.write (f"Base membership cost: {base_price:.2f}\n" )
                f.write (f"Extra cost: {extras_total:.2f}\n")
                f.write (f"Total Discount: {total_discount:.2f}\n")
                f.write (f"Total cost: {total:.2f}\n")
                f.write (f"Weekly cost : {weekly_cost:.2f}\n")
                f.write (f"Payment due: {total:.2f}\n")
                f.write (f"----------------------------------\n\n")

        except:
            print("An error has occured.")

        clearform()#clears the form for another submission
          
        
def clearform():
    messagebox.showinfo("The Aurora Archive", "Thank you for visiting.")  
    #clearing values on entry boxes
    entry_first_name.delete(0, tkinter.END)
    entry_last_name.delete(0, tkinter.END)
    entry_address.delete(0, tkinter.END)
    entry_mobile.delete(0, tkinter.END)
    entry_library_number.delete(0, tkinter.END)

    #resetting the radio buttons
    membership_plan.set(plan_standard)
    payment_plan.set(plan_monthly)

    #resetting check buttons
    extra1.set(False)
    extra2.set(False)
    extra3.set(False)
    extra4.set(False)
    has_library_card.set(False)

    #resetting the values to default which is "--"
    label_total_cost_base.config(text= "--")
    label_total_cost_extras.config(text= "--")
    label_total_weekly_cost.config(text= "--")
    label_total_cost_annual.config(text= "--")
    label_total_cost_discount.config(text= "--")
    label_total_cost_total.config(text= "--")


#reset function
def reset():
    answer = messagebox.askyesno("Warning!!!", "WARNING!!!\nWould you like to reset your form?")
    if answer:
        #resetting/clearing values on entry boxes
        entry_first_name.delete(0, tkinter.END)
        entry_last_name.delete(0, tkinter.END)
        entry_address.delete(0, tkinter.END)
        entry_mobile.delete(0, tkinter.END)
        entry_library_number.delete(0, tkinter.END)

        #resetting the radio buttons
        membership_plan.set(plan_standard)
        payment_plan.set(plan_monthly)

        #resetting check buttons
        extra1.set(False)
        extra2.set(False)
        extra3.set(False)
        extra4.set(False)
        has_library_card.set(False)

        #resetting the values to default which is "--"
        label_total_cost_base.config(text= "--")
        label_total_cost_extras.config(text= "--")
        label_total_weekly_cost.config(text= "--")
        label_total_cost_annual.config(text= "--")
        label_total_cost_discount.config(text= "--")
        label_total_cost_total.config(text= "--")

        return



# _____________________________----
# Widget definitions
# _____________________________----
# The widget definitions are found in this section, no positioning has been done here, just declaration


#### Labels ####

label_first_name = tkinter.Label(window, text = "First Name:", font= ("sofia", 10))
label_last_name = tkinter.Label(window, text = "Last Name:", font= ("sofia", 10))
label_address = tkinter.Label(window, text = "Address:", font= ("sofia", 10))
label_mobile = tkinter.Label(window, text = "Mobile:", font= ("sofia", 10))

label_membership_type = tkinter.Label(window, text = "Membership Plan:", font= ("sofia", 10))
label_membership_payment_plan = tkinter.Label(window, text = "Payment Plan:", font= ("sofia",10))
label_library_card = tkinter.Label(window, text = "Library Card:", font= ("sofia", 10))
label_library_number = tkinter.Label(window, text = "Card Number:", font= ("sofia", 10))

label_optional_extras = tkinter.Label(window, text = "Optional Extras:", font= ("sofia", 10))

label_total_header = tkinter.Label(window, text = "Totals", width= 5, height= 2, font= ("sofia", 10))
label_total_base = tkinter.Label(window, text = "Membership Cost:", font= ("sofia", 10))
label_total_extras = tkinter.Label(window, text = "Extra Charges:", font= ("sofia", 10))
label_total_annual = tkinter.Label(window, text = "Annual Cost:", font= ("sofia", 10))
label_total_discount = tkinter.Label(window, text = "Total Discount:", font= ("sofia", 10))
label_weekly_cost = tkinter.Label(window, text= "Weekly Cost", font =("Sofia", 10))
label_total_final = tkinter.Label(window, text = "Total Cost:", font= ("sofia", 10))


label_total_cost_base = tkinter.Label(window, text = "--")
label_total_cost_extras = tkinter.Label(window, text = "--")
label_total_weekly_cost = tkinter.Label(window, text = "--")
label_total_cost_annual = tkinter.Label(window, text = "--")
label_total_cost_discount = tkinter.Label(window, text = "--")
label_total_cost_total = tkinter.Label(window, text = "--")


label_redasterisk_1 = tkinter.Label(window, text= "*", fg= "red")
label_redasterisk_2 = tkinter.Label(window, text= "*", fg= "red")
label_redasterisk_3 = tkinter.Label(window, text= "*", fg= "red")
label_redasterisk_4 = tkinter.Label(window, text= "*", fg= "red")
label_redasterisk_5 = tkinter.Label(window, text= "*", fg= "red")
label_mandetory = tkinter.Label (window, text = "NOTE: Fields with \"*\" are mandatory.", fg = "red")

label_line1 = tkinter.Label(window, text= "_____________________________")
label_line2 = tkinter.Label(window, text= "_____________________________")

#### Entry text boxes ####

entry_first_name = tkinter.Entry(window)
entry_last_name = tkinter.Entry(window)
entry_address = tkinter.Entry(window)
entry_mobile = tkinter.Entry(window)

entry_library_number = tkinter.Entry(window)

#### Radio buttons ####
#added command = calculation to auto calculate after clients request.
radio_membership_1 = tkinter.Radiobutton(window, text = plan_standard, variable = membership_plan, value = plan_standard, command= calculate)
radio_membership_2 = tkinter.Radiobutton(window, text = plan_premium, variable = membership_plan, value = plan_premium, command= calculate)
radio_membership_3 = tkinter.Radiobutton(window, text = plan_kids, variable = membership_plan, value = plan_kids, command= calculate)

radio_payment_plan_1 = tkinter.Radiobutton(window, text = plan_monthly, variable = payment_plan, value = plan_monthly, command= calculate)
radio_payment_plan_2 = tkinter.Radiobutton(window, text = plan_annual, variable = payment_plan, value = plan_annual, command= calculate)

#### Checkbuttons ####
#added command = calculation to auto calculate after clients request.
checkbutton_has_library_card = tkinter.Checkbutton(window, text = "", variable = has_library_card, onvalue = True, offvalue = False, command= calculate)

checkbutton_extra1 = tkinter.Checkbutton(window, text = optional_1, variable = extra1, onvalue = True, offvalue = False, command= calculate)
checkbutton_extra2 = tkinter.Checkbutton(window, text = optional_2, variable = extra2, onvalue = True, offvalue = False, command= calculate)
checkbutton_extra3 = tkinter.Checkbutton(window, text = optional_3, variable = extra3, onvalue = True, offvalue = False, command= calculate)
checkbutton_extra4 = tkinter.Checkbutton(window, text = optional_4, variable = extra4, onvalue = True, offvalue = False, command= calculate)


#### Buttons ####

button_calculate = tkinter.Button(window, text = "Calculate", command = calculate, font= ("sofia", 10), bg= "yellow")
button_submit = tkinter.Button(window, text = "Submit", command = submit,font= ("sofia", 10), bg= "green")
button_reset = tkinter.Button (window, text= "Reset", command= reset,font= ("sofia", 10), bg= "red")


# _____________________________----
# Widget positioning
# _____________________________----

label_mandetory.grid(row = 0, column = 0, columnspan= 3)
label_first_name.grid(row = 1, column = 0, sticky = "w")
label_redasterisk_1.grid(row = 1, column= 0, sticky= "ne" )
label_last_name.grid(row = 2, column = 0, sticky = "w")
label_redasterisk_2.grid(row = 2, column= 0, sticky= "ne" )
label_address.grid(row = 3, column = 0, sticky = "w")
label_redasterisk_3.grid(row = 3, column= 0, sticky= "ne" )
label_mobile.grid(row = 4, column = 0, sticky = "w")
label_redasterisk_4.grid(row = 4, column= 0, sticky= "ne" )


label_membership_type.grid(row = 5, column = 0, sticky = "w")
label_membership_payment_plan.grid(row = 8, column = 0, sticky = "w")
label_library_card.grid(row = 16, column = 0, sticky = "w")

entry_first_name.grid(row = 1, column = 1, sticky = "w")
entry_last_name.grid(row = 2, column = 1, sticky = "w")
entry_address.grid(row = 3, column = 1, sticky = "w")
entry_mobile.grid(row = 4, column = 1, sticky = "w")

radio_membership_1.grid(row = 5, column = 1, sticky = "w")
radio_membership_2.grid(row = 6, column = 1, sticky = "w")
radio_membership_3.grid(row = 7, column = 1, sticky = "w")

radio_payment_plan_1.grid(row = 8, column = 1, sticky = "w")
radio_payment_plan_2.grid(row = 9, column = 1, sticky = "w")

label_optional_extras.grid(row = 12, column = 0, sticky = "w")
checkbutton_extra1.grid(row = 12, column = 1, sticky = "w")
checkbutton_extra2.grid(row = 13, column = 1, sticky = "w")
checkbutton_extra3.grid(row = 14, column = 1, sticky = "w")
checkbutton_extra4.grid(row = 15, column = 1, sticky = "w")

label_library_number.grid(row = 17, column = 0, sticky = "w")
checkbutton_has_library_card.grid(row = 16, column = 1, sticky = "w")
entry_library_number.grid(row = 17, column = 1, sticky = "w")

label_total_header.grid(row = 20, column = 0, sticky = "w")
label_total_base.grid(row = 21, column = 0, sticky = "w")
label_total_extras.grid(row = 22, column = 0, sticky = "w")
label_weekly_cost.grid(row= 23, column= 0, sticky= "w")
label_total_annual.grid(row = 24, column = 0, sticky = "w")
label_total_discount.grid(row = 25, column = 0, sticky = "w")
label_total_final.grid(row = 26, column = 0, sticky = "w")

label_total_cost_base.grid(row = 21, column = 1, sticky = "w")
label_total_cost_extras.grid(row = 22, column = 1, sticky = "w")
label_total_weekly_cost.grid (row = 23, column=1, sticky = "w")
label_total_cost_annual.grid(row = 24, column = 1, sticky = "w")
label_total_cost_discount.grid(row = 25, column = 1, sticky = "w")
label_total_cost_total.grid(row = 26, column = 1, sticky = "w")

label_line1.grid(row= 27, column= 0)
label_line2.grid(row= 27, column= 1)
button_calculate.grid(row = 28, column = 1)
button_submit.grid(row = 28, column = 0, padx= 5, ipadx= 5)
button_reset.grid(row = 28, column = 0, columnspan= 3)


# _____________________________--------
# Tkinter mainloop
window.mainloop()
