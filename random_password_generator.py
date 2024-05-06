# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:20:40 2024

@author: uppal
"""

import tkinter as tk
from tkinter import messagebox
from random import choice, shuffle

def generate_password():
    global letter_size, num_size, special_char_size
    global password_length

    letter_size = int(letter_entry.get())
    num_size = int(num_entry.get())
    special_char_size = int(special_char_entry.get())

    password_length = letter_size + num_size + special_char_size

    if password_length == 0:
        messagebox.showerror("Error", "The password cannot be empty.")
    else:
        password = ""

        for _ in range(letter_size):
            password += choice(letters)

        for _ in range(num_size):
            password += choice(numbers)

        for _ in range(special_char_size):
            password += choice(special_chars)

        password_list = list(password)
        shuffle(password_list)

        password = ""

        for i in password_list:
            password += i

        generated_password_label.config(text="Generated Password: " + password)
 
# GUI setup
root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg="red")  # Set background color

main_frame = tk.Frame(root, bg="#f0f0f0")  # Set background color for the frame
main_frame.pack(padx=100, pady=100)

tk.Label(main_frame, text="Letters:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
letter_entry = tk.Entry(main_frame)
letter_entry.grid(row=0, column=1)

tk.Label(main_frame, text="Numbers:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
num_entry = tk.Entry(main_frame)
num_entry.grid(row=1, column=1)

tk.Label(main_frame, text="Special Characters:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
special_char_entry = tk.Entry(main_frame)
special_char_entry.grid(row=2, column=1)

generate_button = tk.Button(main_frame, text="Generate Password", command=generate_password, bg="red", fg="white")  # Set button color
generate_button.grid(row=3, columnspan=2, pady=10)

generated_password_label = tk.Label(main_frame, text="", bg="grey")
generated_password_label.grid(row=4, columnspan=2)

# Character sets
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "~!@#$%^&*"

root.mainloop()