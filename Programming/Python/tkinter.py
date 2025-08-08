
#displaying a messagebox
#import tkinter

import tkinter as tk
from tkinter import messagebox

messagebox.showinfo ("Your message box title", "This is the messagebox text!")

window = tk.Tk()
window.title("Your title here")
window.mainloop()




#Using grid to make a label look like a telephone number
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



#using place to make a face and greeting message
import tkinter as tk 
root = tk.Tk() 
root.title("Place example")  
 

left_eye = tk.Label(root, text = "O") 
right_eye = tk.Label(root, text = "O")
mouth = tk.Label(root, text = "____")


message = tk.Label(root, text = "Greetings!") 

 
# Position left eye 
left_eye.place(x = 0, y = 20 ) 
# Position right eye 
right_eye.place(x = 40, y = 20) 
# Position mouth 
mouth.place(x = 15, y = 24) 
# Position message 
message.place(x = 0, y = 60) 



root.mainloop()



#using pack to place the buttons

import tkinter as tk 
root = tk.Tk() 
root.title("Pack example") 

button1 = tk.Button(text = "*****") 
button2 = tk.Button(text = "**") 
button3 = tk.Button(text = "*") 
button4 = tk.Button(text = "****") 
button5 = tk.Button(text = "***") 

# Add your pack statements here
button3.pack ()
button2.pack ()
button5.pack ()
button4.pack ()
button1.pack ()
 
root.mainloop()



