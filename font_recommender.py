import requests
import pandas as pd
import os
import time
import urllib.request
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import numpy as np
from tkinter import *

# Google Fonts API (replace with your API key)
api_token = "YOUR_GOOGLE_FONTS_API_KEY"

# API url 

api_url = f"https://www.googleapis.com/webfonts/v1/webfonts?key={api_token}&sort=popularity"

# Fetch font data
try:
    response = requests.get(api_url)
    response.raise_for_status() #ensures successful response
    font_data = response.json()
    font_families = font_data.get("items", [])
except (requests.exceptions.RequestException, ValueError) as e:
    print(f"Error fetching font data: {e}")
    font_families = []  # default to empty list if response fails


# get relevant font info

font_info = []
for font in font_families:
    info = {
        "family": font.get("family"),
        "variants": font.get("variants"),
        "subsets": font.get("subsets"),
        "category": font.get("category")
    }
    font_info.append(info)

#create root window
root = Tk()
root.title("Font Recommender")
root.geometry('450x350')

#labels
Label(root, text='Variants').grid(row=0, column=0, padx=10, pady=5)
Label(root, text='Subsets').grid(row=1, column=0, padx=10, pady=5)
Label(root, text='Category').grid(row=2, column=0, padx=10, pady=5)

#entry fields

variants_entry = Entry(root, width=20)
variants_entry.grid(column=1, row=0, padx=10, pady=5)

subsets_entry = Entry(root, width=20)
subsets_entry.grid(column=1, row=1, padx=10, pady=5)

category_entry = Entry(root, width=20)
category_entry.grid(column=1, row=2, padx=10, pady=5)

#result label

result_label = Label(root, text="", wraplength=300, justify="left")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

#functions to recommend fonts based on user input
def recommend_fonts():
    variants = variants_entry.get().strip().lower()
    subsets = subsets_entry.get().strip().lower()
    category = category_entry.get().strip().lower()

    user_fonts = []
    for font in font_info:
        variants_match = not variants or variants.lower() in [v.lower() for v in font["variants"]]
        subsets_match = not subsets or subsets.lower() in [s.lower() for s in font["subsets"]]
        category_match = not category or category.lower() in font["category"]


        if variants_match and subsets_match and category_match:
            user_fonts.append(font["family"])

            
    # Display recommended fonts
    if user_fonts:
        recommendation_text = "\n".join(user_fonts[:10])  # Display top 10 recommended fonts
        result_label.config(text="Recommended Fonts:\n" + recommendation_text)
    else:
        result_label.config(text="No fonts matching requirements")

#button to get recommendations

Button(root, text='Font Recommendations', command=recommend_fonts).grid(row=3, column=0, columnspan=2, pady=10)

#execution of Tkinter

root.mainloop()
