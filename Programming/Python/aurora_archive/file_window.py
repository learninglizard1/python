import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import csv


data_file = None
member_list = []


def open_file():
    global data_file
    global member_list

    data_file = fd.askopenfile(filetypes= [("CSV Files", "*.csv"), ("All Files", "*.*")])
    # Check to ensure file has been selected
    if (data_file is not None):
        # Read the file using CSV reader
        csv_reader = csv.reader(data_file)
        # Only continue if the reader is not empty
        if (csv_reader):
            # Reset the member_list
            member_list = []

        # Loop through the rows and print each row to test
        for row in csv_reader:
            # Looop through the csv_reader and add each row round into our member_list variable
            if (len(row)< 1): # Skip rows that are blank
                continue
            member_list.append (row)


def save_file():
    global data_file
    global member_list
    # Check if a file has been opened first
    if (not data_file):
        mb.showerror(title="Warning", message= "You must open a file first.")
        return

    file = fd.asksaveasfile(initialfile = data_file.name, defaultextension= ".csv", filetypes= [("CSV Files", "*.csv"), ("All Files", "*.*")])
    # Only proceed if a file was selected
    if (file):
        # Open file for writing
        # We will overwrite the fiel rather than append
        with open (file.name, "w") as new_file:
            # Create a csv writer so we can write to the file using csv
            csv_writer = csv.writer(new_file)
            for row in member_list:
                # Loop through our member_list and write a row for each member
                csv_writer.writerow(row)
