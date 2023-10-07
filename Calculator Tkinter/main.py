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


btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial",14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial",14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial",14))
btn_3.grid(row=2, column=3)
root.mainLoop()
