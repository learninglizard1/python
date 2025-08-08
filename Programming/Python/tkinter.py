
#displaying a messagebox
#import tkinter

import tkinter as tk
from tkinter import messagebox

messagebox.showinfo ("Your message box title", "This is the messagebox text!")

window = tk.Tk()
window.title("Your title here")
window.mainloop()




#creating a labels like a telephone number
#import tkinter

import tkinter as tk

root = tk.Tk()

#create 2 label widgets
label1 = tk.Label(root, text = "1")
label2 = tk.Label(root, text = "2")
label3 = tk.Label (root, text = "3")
label4 = tk.Label (root, text = "4")
label5 = tk.Label (root, text = "5")
label6 = tk.Label (root, text = "6")
label7 = tk.Label (root, text = "7")
label8 = tk.Label (root, text = "8")
label9 = tk.Label (root, text = "9")


#positioning the widgets
label1.grid (row = 0, column = 0) #position at cell 0,0
label2.grid (row = 0, column = 1) #position at cell 0,1
label3.grid (row = 0, column = 2) #position at cell 0,2
label4.grid (row = 1, column = 0) #position at cell 1,0
label5.grid (row = 1, column = 1) #position at cell 1,1
label6.grid (row = 1, column = 2) #position at cell 1,2
label7.grid (row = 2, column = 0) #position at cell 2,0
label8.grid (row = 2, column = 1) #position at cell 2,1
label9.grid (row = 2, column = 2) #position at cell 2,2

root.mainloop()
