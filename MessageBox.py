import tkinter as tk
from tkinter import messagebox

class MyGUI:
	
	def __init__(self):
		
		self.root = tk.Tk()
		
		self.label = tk.Label(self.root, text ="Your Message", font =("Arial", 18))
		self.label.pack(padx = 10, pady =10)
		
		self.textbox = tk.Text(self.root, height =1.5, font=("Arial",16))
		self.textbox.pack(padx =10, pady =10)
		
		self.checkState = tk.IntVar()
		
		self.check = tk.Checkbutton(self.root, text ="Show Messagebox", font=("Arial", 16), variable = self.checkState)
		self.check.pack(padx =0, pady = 0)
		
		self.button = tk.Button(self.root, text="Show Mesage", font=("Arial",16), command = self.show_message)
		self.button.pack(padx =10, pady =10)
		
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		
		
		self.root.mainloop()
		
	def show_message(self):
		if self.checkState.get() ==  0:
			print(self.textbox.get("1.0", tk.END))
			
		else:
				messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))
		   
	def on_closing(self):
		print()
		#	if messagebox.askyesno(title="Quit?"message ="Do you really want to quit?"):
		#	self.root.destroy()
				
				
				
MyGUI()
