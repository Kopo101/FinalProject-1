"""
This is the file that containes all of the code for the main interface 
"""

from tkinter import *
from tkinter import ttk
root = Tk()

#Global Variables
global canvas_width
global canvas_height
global number_of_days
global hours_in_day

canvas_width = 600
canvas_height = 400
number_of_days = 7
hours_in_day = 10

# Buttons we will ned
create_new = ttk.Button(root, text='New Appointment', padding=(5,5,5,5))

# Make frame to hold our canvas
frame = ttk.Frame(root, relief = "sunken", borderwidth = 5, padding=(3,3,3,3))

# Set up our Canvas
canvas = Canvas(frame, width = canvas_width, height=canvas_height)

#A loop to create a grid
for i in range(0,canvas_height+1, canvas_height//hours_in_day):
	canvas.create_line(0, i, canvas_width, i, tags=('grid', 'HorizontalLines'))
for i in range(0,canvas_width+1,canvas_width//number_of_days):
	canvas.create_line(i, 0, i, canvas_height, tags =('grid', 'VirticleLines'))

#Create all the labels we will need
sunday = ttk.Label(text='Sunday')
monday = ttk.Label(text='Monday')
tuesday = ttk.Label(text='Tuesday')
wednesday = ttk.Label(text='Wednesday')
thursday = ttk.Label(text="Thursday")
friday = ttk.Label(text='Friday')
saturday = ttk.Label(text = 'Saturday')

#------------------------------------------grid all widgets------------------------------------------------
#Frame
frame.grid(column = 1, row = 1, columnspan = 7, rowspan= 10) 

#canvas
canvas.grid()
#grid
create_new.grid(column= 0, row=0)

#days of the week
sunday.grid(column=1, row=0)
monday.grid(column=2, row=0)
tuesday.grid(column=3, row=0)
wednesday.grid(column=4, row=0)
thursday.grid(column=5,row=0)
friday.grid(column=6, row=0)
saturday.grid(column=7, row=0)

root.mainloop()	