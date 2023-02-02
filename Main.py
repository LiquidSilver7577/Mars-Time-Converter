# UI for Martian time conversion

# Import tkinter for GUI
import tkinter as tk
from tkinter import messagebox

# Define Martian time conversion rate
martian_conversion = 1.03

def convert_time():
    # Get Earth time from input field
    earth_time = input_field.get()

    # Split input into hours and minutes
    time_list = earth_time.split(":")
    hours = int(time_list[0])
    minutes = int(time_list[1])

    # Convert Earth hours to Martian hours
    martian_hours = int(hours * martian_conversion)

    # Convert Earth minutes to Martian minutes
    martian_minutes = int(minutes * martian_conversion)

    # Handle overflow from minutes to hours
    while martian_minutes >= 60:
        martian_hours += 1
        martian_minutes -= 60

    # Handle overflow from hours to 24
    while martian_hours >= 24:
        martian_hours -= 24

    # Format Martian time for output
    martian_time = "{:02d}:{:02d}".format(martian_hours, martian_minutes)

    # Display Martian time in output field
    output_field.config(text=martian_time)

# Create main window
root = tk.Tk()
root.title("Martian Time Converter")

# Create input field
input_field = tk.Entry(root, width=10)
input_field.pack()

# Create convert button
convert_button = tk.Button(root, text="Convert", command=convert_time)
convert_button.pack()

# Create output field
output_field = tk.Label(root, text="")
output_field.pack()

# Start main loop
root.mainloop()
