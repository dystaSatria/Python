import tkinter as tk


calculation = ""

def addCalculation(symbol):
  global calculation
  calculation += str(symbol)
  textResult.delete(1.0, "end")
  textResult
  

def eventCalculation(symbol):
  global calculation
  try: 
    calculation = str(eval(calculation))
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
  except: 
    clear_field()
    text_result.insert(1.0,"Error")
    pass

def clearField():
  global calculation
  calculation = ""
  text_result.delete(1.0,"end")
  pass


root = tk.TK()
root.geometry("300x275")


textResult = tk.Text(root, height=2, width=16, font=("Arial",24))  
textResult.grid(columnspan=5)


btn_1 = tk.Button(root, text="1", command=lambda:)
root.mainLoop()
