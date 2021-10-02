import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:

	root = Tk()

	# WIndow
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(root)
	__thisMenuBar = Menu(root)

	# ScrollBar
	__thisScrollBar = Scrollbar(__thisTextArea)
	__file = None

	def __init__(self,**kwargs):

		# Window Size
		self.__thisWidth = kwargs['width']
		self.__thisHeight = kwargs['height']

		# Window Title
		self.root.title("Untitled - Notepad")

		# WIndow Alignment
		screenWidth = self.root.winfo_screenwidth()
		screenHeight = self.root.winfo_screenheight()

		left = (screenWidth / 2) - (self.__thisWidth / 2)
		top = (screenHeight / 2) - (self.__thisHeight / 2)

		self.root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
											self.__thisHeight,
											left, top))

		# Resizable 
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_columnconfigure(0, weight=1)

		self.__thisTextArea.grid(sticky= N + E + S + W)

		# New File
		self.__thisMenuBar.add_command(label="New", 
										command=self.__newFile)

		# Existing File
		self.__thisMenuBar.add_command(label="Open",
										command=self.__openFile)

		# Save File
		self.__thisMenuBar.add_command(label="Save",
										command=self.__saveFile)

		# Exit
		self.__thisMenuBar.add_command(label="Exit",
										command=self.__quitApplication)

		self.root.config(menu=self.__thisMenuBar)
		self.__thisScrollBar.pack(side=RIGHT,fill=Y)

		# ScrollBar Adjustment
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

	
	def __quitApplication(self):
		self.__root.destroy()

	def __openFile(self):

		self.__file = askopenfilename(defaultextension=".txt",
									filetypes=[("All Files","*.*"),
									("Text Documents","*.txt")])

		
		if self.__file == "":

			self.__file = None

		else:

			self.root.title(os.path.basename(self.__file) + " - Notepad")
			self.__thisTextArea.delete(1.0,END)

			file = open(self.__file,"r")

			self.__thisTextArea.insert(1.0,file.read())

			file.close()

		
	def __newFile(self):
		self.root.title("Untitled - Notepad")
		self.__file = None
		self.__thisTextArea.delete(1.0,END)

	def __saveFile(self):

		if self.__file == None:
			self.__file = asksaveasfilename(initialfile="Untitled.txt",
											defaultextension=".txt",
											filetypes=[("All Files","*.*"),
												("Text Document","*.txt")])

			if self.__file == "":
				self.__file = None
			else:

				file = open(self.__file,"w")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()

				self.root.title(os.path.basename(self.__file) + " - Notepad")

		else:
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()

	def run(self):

		# Main Application
		self.root.mainloop()


# Run Main Application
notepad = Notepad(width=600,height=400)
notepad.run()