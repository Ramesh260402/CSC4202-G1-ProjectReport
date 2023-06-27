
import tkinter as tk
from tkinter import messagebox
from graph import Graph as g
from reader import Reader as r
from scheduleui import GraphUI

def check_valid(credits, start_sem):
    # Checks to see if the csv format is good
    if not read_major.valid_format[0]:
        messagebox.showerror("Error", read_major.valid_format[1])
        return False
    
    # Checks that the input for credits is a number
    if not credits.isnumeric() and credits != '':
        message = "Invalid input. Please enter a number."
        messagebox.showerror("Error", message)
        return False

    # Checks to make sure that the input for start_sem is a number
    if not start_sem.isdigit() and start_sem != '':
        message = "Invalid input. Please enter a positive integer"
        messagebox.showerror("Error", message)
        return False
    
    return True

# Writes the schedule to a file
def create_schedule_file(schedule):
    file = open("generated_schedule.txt", 'w')
    file.write(str(schedule))
    file.close()

# Button press function
def button_press(file_name, credits, start_sem):
    # Clear the previous data
    read_major.clear()
    read_major.read(file_name)
    
    # Display a message about full screen mode
    messagebox.showwarning("INFO", "When the program runs, the graph will be set to fullscreen.\nTo close this window please use CTL-F, (or CMD-W for Mac)")

    if check_valid(credits, start_sem):
        # Create the graph and perform topological sorting
        graph_make.create_graph(read_major.courseDict) 
        graph_make.create_top_sort()
        
        # Generate the course schedule
        schedule = graph_make.create_schedule(credits, start_sem)

        # Output schedule to a text file
        create_schedule_file(schedule)

        # Display the graph
        class_display = GraphUI(schedule, read_major)
        class_display.create_graph()

# Create the UI
root = tk.Tk()
root.geometry("500x300")
root.title("Course Schedule")
root.eval('tk::PlaceWindow . center')

# Create a label for the input file
label_file = tk.Label(root, text="Input File:")
label_file.pack()

# Create an entry field for the input file
entry_file = tk.Entry(root)
entry_file.pack()

# Create a label for credits per semester
label_credit = tk.Label(root, text="Credits per semester:")
label_credit.pack()

# Create an entry field for credits per semester
entry_credit = tk.Entry(root)
entry_credit.pack()

# Create a label for the starting semester
label_start = tk.Label(root, text="Starting semester:")
label_start.pack()

# Create an entry field for the starting semester
entry_start = tk.Entry(root)
entry_start.pack()

# Create instances of the reader and graph classes
read_major = r()
graph_make = g()

# Create a button that calls the button_press function
button_generate = tk.Button(root, text="Generate schedule (graph)", command=lambda:[button_press(entry_file.get(), entry_credit.get(), entry_start.get())])
button_generate.pack()

root.mainloop()