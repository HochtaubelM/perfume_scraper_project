#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:50:16 2024

@author: maria hochtaubel
"""

import customtkinter as ctk
from tkinter import messagebox, ttk
from ParfumScraper import PerfumeScraper  
import pandas as pd

# Dictionary with perfume URLs - add more as needed
urls = {
    "Burberry Goddess": 'https://www.perfumehub.pl/burberry-goddess-woda-perfumowana-dla-kobiet-100-ml',
    "Chloe Lumineuse": 'https://www.perfumehub.pl/chloe-chloe-lumineuse-woda-perfumowana-dla-kobiet-100-ml',
    "Burberry Her London Dream": 'https://www.perfumehub.pl/burberry-her-london-dream-woda-perfumowana-dla-kobiet',
    "Dior Homme": 'https://www.perfumehub.pl/dior-dior-homme-woda-toaletowa-dla-mezczyzn-100-ml'
}

# Create main application window
app = ctk.CTk()
app.geometry("600x400") 
app.title("Perfume Data Scraper")

# Fetch perfume data
def get_data():
    selected_perfume = perfume_var.get() # Get perfume selected by the user in the dropdown
    if not selected_perfume:
        messagebox.showwarning("Error", "Please select a perfume") # Display warning if none selected
        return

    url = urls[selected_perfume]  # Get URL for the selected perfume
    scraper = PerfumeScraper(url) # Create PerfumeScraper object with URL for selected perfume
    
    try:
        df = scraper.run()  # Fetch data and create DataFrame
        display_data(df)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while downloading data: {e}")

# Function to display data in a Treeview table
def display_data(df):
    # Clear previous data from the frame
    for widget in data_frame.winfo_children():
        widget.destroy()

    # Create table with column headers
    columns = list(df.columns)
    tree = ttk.Treeview(data_frame, columns=columns, show="headings", height=10)

    # Set up headers and align columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    # Populate table with DataFrame data
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    # Add vertical scrollbar if needed
    scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Pack the table into the frame
    tree.pack(fill="both", expand=True)

# Set up GUI elements
perfume_var = ctk.StringVar(value="")
perfume_label = ctk.CTkLabel(app, text="Select Perfume:")
perfume_label.pack(pady=(20, 5))

perfume_dropdown = ctk.CTkComboBox(app, variable=perfume_var, values=list(urls.keys()))
perfume_dropdown.pack(pady=5)

get_data_button = ctk.CTkButton(app, text="Fetch Data", command=get_data)
get_data_button.pack(pady=10)

data_frame = ctk.CTkFrame(app)
data_frame.pack(pady=20, fill="both", expand=True)

# Start main application loop
app.mainloop()
