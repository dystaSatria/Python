import re
import tkinter as tk
from tkinter import filedialog
from docx import Document

def read_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return text

def extract_prices(text):
    price_pattern = r'Price:\s*\$([\d,]+\.\d{2})'
    prices = []

    for line in text:
        matches = re.findall(price_pattern, line)
        for match in matches:
            price = float(match.replace(',', ''))
            prices.append(price)

    return prices

def sort_prices():
    file_path = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
    text = read_text_from_docx(file_path)
    prices = extract_prices(text)
    sorted_prices = sorted(prices)

    
    result_text.delete(1.0, tk.END)  
    result_text.insert(tk.END, "Sorted Prices:\n")
    for price in sorted_prices:
        result_text.insert(tk.END, f"Price: ${price:.2f}\n")

root = tk.Tk()
root.title("Price Sorting Application")

browse_button = tk.Button(root, text="Choose Document File", command=sort_prices)
browse_button.pack(pady=10)

result_text = tk.Text(root, height=10, width=40)
result_text.pack()

root.mainloop()
