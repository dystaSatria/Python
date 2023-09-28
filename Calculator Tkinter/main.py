import tkinter as tk


calculation = ""

def addCalculation(symbol):
  global calculation
  calculation += str(symbol)
  textResult.delete(1.0, "end")
  textResult
  

def eventCalculation(symbol):
  pass

def clearField():
  pass


root = tk.TK()
root.geometry("300x275")


textResult = tk.Text(root, height=2, width=16, font=("Arial",24))  
textResult.grid(columnspan=5)
root.mainLoop()
