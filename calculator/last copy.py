#import tkinter and math and os 
from tkinter import *
import math
import os
#make the parent widget
root = Tk()

#add an icon 
root.iconbitmap('Solar-Power-Calculator-Desktop-Office-Calculator-Color-Custom-Logo (1).ico')




# set the name of the calculator
root.title("power  mahy Calculator")

# sets the background color of the calculator
root.configure(background = 'pink')

# make the calculator can stretched
root.resizable(width=True, height=True)

# sets the geometry
root.geometry("480x586+450+90")

# holds the buttons in the calculator,
# act as a container for numbers and operators
calc = Frame(root)

calc.grid()
#import the webbrowser
import webbrowser
import tkinter.messagebox
#create a class includes the functions
class Calc():
	#intilization 
	def __init__(self):
		self.total = 0
		self.current = ''
		self.input_value = True
		self.check_sum = False
		self.op = ''
		self.result = False

	def numberEnter(self, num):
		self.result = False
		firstnum = txtDisplay.get()
		secondnum = str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value = False
		else:
			if secondnum == '.':
				if secondnum in firstnum:
					return
			self.current = firstnum+secondnum
		self.display(self.current)

	def sum_of_total(self):
		self.result = True
		self.current = int(self.current)
		if self.check_sum == True:
			self.valid_function()
		else:
			self.total = float(self.current)
#from which index the output can be deleted and can be inserted
	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)
#specify the operations and their roles
	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
		self.input_value = True
		self.check_sum = False
		self.display(self.total)
#what to do if the operation is not valid
	def operation(self, op):
		self.current = int(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total = self.current
			self.input_value = True
		self.check_sum = True
		self.op = op
		self.result = False
#declare the function delete there is no thing will show when delete 
	def delete(self):
		self.result = False
		self.current = None
		self.display(self.current)
		self.input_value = True

	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)

	def tau(self):
		self.result = False
		self.current = math.tau
		self.display(self.current)
#
	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)

	def mathPM(self):
		self.result = False
		self.current = -(int(txtDisplay.get()))
		self.display(self.current)
#declare the function squared it takes the entered number and shows the self current
	def squared(self):
		self.result = False
		self.current = math.sqrt(int(txtDisplay.get()))
		self.display(self.current)
#declare the function cos it takes the entered number and shows the self current
	def cos(self):
		self.result = True
		self.current = math.cos(math.radians(int(txtDisplay.get())))
		self.display(self.current)

	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(int(txtDisplay.get())))
		self.display(self.current)
#declare the function tan it takes the entered number and shows the self current
	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(int(txtDisplay.get())))
		self.display(self.current)

	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(int(txtDisplay.get())))
		self.display(self.current)

	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(int(txtDisplay.get())))
		self.display(self.current)
#declare the function sinh it takes the entered number and shows the self current
	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(int(txtDisplay.get())))
		self.display(self.current)

	def log(self):
		self.result = False
		self.current = math.log(int(txtDisplay.get()))
		self.display(self.current)
#declare the function exp it takes the entered number and shows the self current
	def exp(self):
		self.result = False
		self.current = math.exp(int(txtDisplay.get()))
		self.display(self.current)


	def expm1(self):
		self.result = False
		self.current = math.expm1(int(txtDisplay.get()))
		self.display(self.current)

	def lgamma(self):
		self.result = False
		self.current = math.lgamma(int(txtDisplay.get()))
		self.display(self.current)
#declare the function degrees it takes the entered number and shows the self current
	def degrees(self):
		self.result = False
		self.current = math.degrees(int(txtDisplay.get()))
		self.display(self.current)
#declare the function log2 it takes the entered number and shows the self current
	def log2(self):
		self.result = False
		self.current = math.log2(int(txtDisplay.get()))
		self.display(self.current)
#declare the function log10 it takes the entered number and shows the self current
	def log10(self):
		self.result = False
		self.current = math.log10(int(txtDisplay.get()))
		self.display(self.current)
#declare the function log1p it takes the entered number and shows the self current
	def log1p(self):
		self.result = False
		self.current = math.log1p(int(txtDisplay.get()))
		self.display(self.current)
#declare the function memory it open a file and write into it
	def memory(self):
		a=open("user memory.txt","a")
		a.write("\n"+txtDisplay.get())
#all these funtions in one class so we call the class
added_value = Calc()

#add the entry and its attributes
txtDisplay = Entry(calc,
				font=('Helvetica', 20,
						'bold'),
				bg='pink',
				fg='black',
				bd=30,
				width=28,
				justify=LEFT)

txtDisplay.grid(row=0,
				column=0,
				columnspan=4,pady=1)


			

# store all the numbers in a variable
numberpad = "123456789"

# here i will count the rows for placing buttons
# in grid
i = 0

# create an empty list to store
# each button with its particular specifications
btn = []

# j is in that range to place
# the button in that particular row
for j in range(2, 5):

		# k is in this range to place the
	# button in that particular column
	for k in range(3):
		btn.append(Button(calc,
						width=6,
						height=2,
						bg='pink',
						fg='white',
						font=('Helvetica', 20, 'bold'),
						bd=4, text=numberpad[i]))

		# set buttons in row & column and
		# separate them with a padding of 1 unit
		btn[i].grid(row=j, column=k, pady=1)

		# put that number as a symbol on that button
		btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
		i += 1

#make the button with command delete
btnClear = Button(calc, text=chr(67),
				width=6, height=2,
				bg='yellow',
				font=('Helvetica', 20, 'bold'),
				bd=4,
				command=added_value.delete).grid(
	row=1, column=0, pady=1)

#make the button with command squared

btnsq = Button(calc, text="\u221A", width=6,
			height=2, bg='yellow',
			font=('Helvetica', 20, 'bold'),
			bd=4, command=added_value.squared).grid(
	row=1, column=1, pady=1)
#add a button with add sympol
btnAdd = Button(calc, text="+", width=6,
				height=2, bg='yellow',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.operation("add")
				).grid(row=1, column=2, pady=1)
#add a button with sub sympol
btnSub = Button(calc, text="-", width=6,
				height=2, bg='yellow',
				font=('Helvetica', 20, 'bold'),
				bd=4,
				command=lambda: added_value.operation("sub")
				).grid(row=2, column=3, pady=1)
#add a button with times sympol
btnMul = Button(calc, text="x", width=6, height=2,
				bg='yellow',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.operation("multi")
				).grid(row=3, column=3, pady=1)
#add a button with division sympol
btnDiv = Button(calc, text="/", width=6,
				height=2, bg='yellow',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.operation("divide")
				).grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=6,
				height=2, bg='yellow', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.numberEnter(0)
				).grid(row=5, column=0, pady=1)
#add a button with dot sympol
btnDot = Button(calc, text=".", width=6,
				height=2, bg='yellow',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.numberEnter(".")
				).grid(row=5, column=1, pady=1)
btnPM = Button(calc, text=chr(177), width=6,
			height=2, bg='yellow',
			font=('Helvetica', 20, 'bold'),
			bd=4, command=added_value.mathPM
			).grid(row=5, column=2, pady=1)
#add a button with equal sympol
btnEquals = Button(calc, text="=", width=6,
				height=2, bg='yellow',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.sum_of_total
				).grid(row=5, column=3, pady=1)
# ROW 1 :
#add these buttons to row 1
btnPi = Button(calc, text="pi", width=6,
			height=2, bg='white', fg='black',
			font=('Helvetica', 20, 'bold'),
			bd=4, command=added_value.pi
			).grid(row=1, column=4, pady=1)

btnCos = Button(calc, text="Cos", width=6,
				height=2, bg='white', fg='black',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.cos
				).grid(row=1, column=5, pady=1)
#add a button to represent the tan
btntan = Button(calc, text="tan", width=6,
				height=2, bg='white', fg='black',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.tan
				).grid(row=1, column=6, pady=1)
#add a button to represent the sin
btnsin = Button(calc, text="sin", width=6,
				height=2, bg='white', fg='black',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.sin
				).grid(row=1, column=7, pady=1)

#make a button with save text to write in the file
btnmemory=Button(calc, text="save", width=6,
				height=2, bg='white', fg='black',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.memory
				).grid(row=1, column=3, pady=1)









# ROW 2 :

btn2Pi = Button(calc, text="2pi", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.tau
				).grid(row=2, column=4, pady=1)
#add a button with cosh text to describe cosh function
btnCosh = Button(calc, text="Cosh", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.cosh
				).grid(row=2, column=5, pady=1)

btntanh = Button(calc, text="tanh", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.tanh
				).grid(row=2, column=6, pady=1)
#add a button with sinh text to describe sinh function
btnsinh = Button(calc, text="sinh", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.sinh
				).grid(row=2, column=7, pady=1)

# ROW 3 :

btnlog = Button(calc, text="log", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.log
				).grid(row=3, column=4, pady=1)
#the row 3 column 5 button to represent the exp function
btnExp = Button(calc, text="exp", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.exp
				).grid(row=3, column=5, pady=1)

btnMod = Button(calc, text="Mod", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.operation("mod")
				).grid(row=3, column=6, pady=1)
#the row 3 column 7 button to represent the efunction
btnE = Button(calc, text="e", width=6,
			height=2, bg='black', fg='white',
			font=('Helvetica', 20, 'bold'),
			bd=4, command=added_value.e
			).grid(row=3, column=7, pady=1)

# ROW 4 :
#row 4 buttons like the other buttons 

btnlog10 = Button(calc, text="log10", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.log10
				).grid(row=4, column=4, pady=1)

btncos = Button(calc, text="log1p", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.log1p
				).grid(row=4, column=5, pady=1)
#a button in row 4column 6 to press it to calculate the expm1
btnexpm1 = Button(calc, text="expm1", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.expm1
				).grid(row=4, column=6, pady=1)

btngamma = Button(calc, text="gamma", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.lgamma
				).grid(row=4, column=7, pady=1)
# ROW 5 :
#a button in row 5column 4 to press it to calculate the log2

btnlog2 = Button(calc, text="log2", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.log2
				).grid(row=5, column=4, pady=1)

btndeg = Button(calc, text="deg", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.degrees
				).grid(row=5, column=5, pady=1)



#creating a label to add a text in the top of functions calculator

lblDisplay = Label(calc, text="scientific calculator",
				font=('Helvetica', 30, 'bold'),
				bg='black', fg='white', justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)





def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("944x568+0+0")

#a funtion with a link to the standard calc
def Standard():
	root.resizable(width=False, height=False)
	root.geometry("480x568+0+0")



#how to enter the youtube channel
def study():
		webbrowser.open("https://www.youtube.com/channel/UCPXsJ97N1UFkyB4_l9a4O8Q")
def openonline():
		webbrowser.open("https://www.desmos.com/scientific")
#a funtion to open the file

def openf():
	
		
		webbrowser.open("user memory.txt")
		# use askyesno function to
# stop/continue the program execution


def iExit():
	iExit = tkinter.messagebox.askyesno("power team calculator",
										"Do you want to exit ?")
	if iExit>0:
		root.destroy()
		os.remove("user memory.txt")
    
		return

#create a menubar 
menubar = Menu(calc)

# ManuBar 1 :

filemenu = Menu(menubar, tearoff = 0)


#the name  of the menu
menubar.add_cascade(label = 'extra options', menu = filemenu)

filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "history", command = openf)
#add a label in the menu with study function
filemenu.add_command(label = "Steps", command = study)
filemenu.add_command(label = "online calculator", command = openonline)


filemenu.add_command(label = "functions", command = Scientific)
#makes the exis separate from others
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)
root.config(menu=menubar)

#close the parent widget
root.mainloop()