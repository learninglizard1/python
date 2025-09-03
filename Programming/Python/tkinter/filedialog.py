import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
from tkinter import filedialog as fd
import csv


root = tk.Tk()
root.geometry("320x240")
root.title("Example program")
root.config(background = "Light Blue")



def menu_file_open ():

    global data_file
    global member_list

    file = fd.askopenfile(filetypes = [("CSV Files", "*.csv"), ("All Files", "*.*")])

    if (file is not None):
        csv_reader= csv.reader(file)
        

        if(csv_reader):
            member_list=[]    

        for row in csv_reader:
            if (len(row)< 1):
                continue
            member_list.append(row)

def menu_file_save():
    
    global data_file
    global member_list

    if (not data_file):
        msgbox.showerror(title = "Warning", mesasge = "You must open a file first." )
        return
    
    file = fd.asksaveasfile(initialfile = data_file.name, defaultextension=".csv", filetypes = [("CSV Files", "*.csv"), ("All Files", ("*.*"))])

    if(file):
        with open (file.name , "w") as new_file:
            csv_writer = csv.writer(new_file)
            for row in member_list:
                csv_writer.writerow(row)

def menu_help_about():
    help=tk.Toplevel(root)  
    help.title("Help")
    help.resizable(False, False)
    lbl_help1=ttk.Label (help, text="About this program\nVsersion 1.0\nSuper Gym Memberships")
    btn_ok=ttk.Button(help, text= "OK", command=help.destroy)
    lbl_help1.grid(row=0, column=0, ipadx=10, ipady=10)
    btn_ok.grid(row=1, column=0, ipadx=5, ipady=5)
    
def menu_member_1():
    print ("Membership > Membership 1")



data_file = ""
member_list = []



menubar = tk.Menu(root)
root.config (menu=menubar)


file_menu = tk.Menu(menubar, tearoff = False)
member_menu = tk.Menu (menubar, tearoff=False)
help_menu = tk.Menu(menubar, tearoff=False)


menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label ="Membership", menu=member_menu)
menubar.add_cascade(label = "Help", menu=help_menu)


file_menu.add_command(label ="Open", command= menu_file_open)
file_menu.add_command(label = "Save", command = menu_file_save)
file_menu.add_separator()

file_menu.add_command(label="Exit", command= root.quit)

member_menu.add_command(label = "Option 1", command=menu_member_1)

help_menu.add_command(label ="About.....", command=menu_help_about)


root.mainloop()

