#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install pandas pillow fpdf


# In[18]:


pip install Pillow


# In[4]:


import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

# Load the CSV file #using jupyter notebook you can upload the csv file in homepage and read it below
df = pd.read_csv('employee_data.csv')

# Create a PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=0)

# Path to the ID card template and font file
template_path = 'C:\\Users\\santo\\Downloads\\IDcardgen\\IDcardtemplate.png' #path to your template
font_path = 'C:\\Windows\\Fonts\\Arial.ttf'  #google font path on your device (for windows same path)

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    # Load the ID card template
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)
    font = ImageFont.truetype(font_path, 20)
    #print(f"Location: {row['Photo Location ']}") #checking if location is found in csv

    # Add name to the template
    draw.text((160, 240), f"Name: {row['Name']}", font= font , fill="black")
    
    # Load and paste the employee's photo
    photo = Image.open(row['Photo Location '])
    photo = photo.resize((186,186))
    template.paste(photo, (264, 1))  # Update coordinates as needed : Photo appears in this coordinates

    # Save the modified template to a temporary image file
    temp_path = f"temp_{index}.png"
    template.save(temp_path)

    # Add a page to the PDF and insert the ID card image
    pdf.add_page()
    pdf.image(temp_path, x=10, y=8, w=180)  # Adjust placement and size as needed

    # Remove the temporary image file after adding to the PDF
    import os
    os.remove(temp_path)

# Output the PDF
pdf.output("C:\\Users\\santo\\Downloads\\Employee_ID_Cards.pdf")
print("PDF 'Employee_ID_Cards' with IDs Generated in Downloads(In template path)")


# In[ ]:




