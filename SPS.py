import tkinter as tk
import random
from tkinter import messagebox
from functools import partial

def write_output(inp,inp1):
	comp=random.randint(0,2)
	if comp==0:
		comp1="ROCK"
	elif comp==1:
		comp1="PAPER"
	elif comp==2:
		comp1="SCISSOR"
	if (inp==0 and comp==2) or (inp==1 and comp==0) or (inp==2 and comp==1):
		messagebox.showinfo("Result","User : "+inp1+"\nComputer : "+comp1+"\nYou Won!")
	elif(inp==0 and comp==1) or (inp==1 and comp==2) or (inp==2 and comp==0):
		messagebox.showinfo("Result","User : "+inp1+"\nComputer : "+comp1+"\nYou Lose!")
	else:
		messagebox.showinfo("Result","User : "+inp1+"\nComputer : "+comp1+"\nIts a TIE!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button_rock = tk.Button(frame,text="ROCK",fg="red",command=partial(write_output,0,"ROCK"))
button_rock.pack(side=tk.LEFT)
button_paper = tk.Button(frame,text="PAPER",fg="red",command=partial(write_output,0,"PAPER"))
button_paper.pack(side=tk.LEFT)
button_scissor = tk.Button(frame,text="SCISSOR",fg="red",command=partial(write_output,0,"SCISSOR"))
button_scissor.pack(side=tk.LEFT)

root.mainloop()
