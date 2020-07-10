from tkinter import *
from tkinter import messagebox
from functools import partial
from sql_functions import sql_func

### initializations and initial setups
sq = sql_func()
window = Tk()
window.geometry('500x450')
window.title('Employee Interest Input')



### string object variables to store the text data
uname = StringVar()
domain = StringVar()
event1 = StringVar()
event2 = StringVar()

i = 0

def submit(uname,domain,event1,event2):
	''' 
	function for button press and store of data
	'''
	MsgBox = messagebox.askquestion ('Submitted','Do you want to Exit?',icon = 'warning')
	if MsgBox == 'yes':
		window.destroy()
	else:
		messagebox.showinfo('Return','You will now return to the screen')
	sq.insert_data(uname.get(),domain.get(),event1.get(),event2.get())
	sq.close()
	return

def get_label_entry(t,tv,i):
	'''
	function to create label and entries widget for the tkinter window
	params:
	t-> text of the label
	tv-> the string variable object to store the user typed data
	i-> to keep track of the row to place the widgets
	'''
	label = Label(window,text=t,height=3,width=10).grid(column=0,row=i)
	entry = Entry(window,textvariable=tv).grid(column=1,row=i)
	return label,entry



uname_label,uname_entry = get_label_entry('Name',uname,i)
i+=1
domain_label,domain_entry = get_label_entry('Domain',domain,i)
i+=1
event1_label,event1_entry = get_label_entry('Event1',event1,i)
i+=1
event2_label,event2_entry = get_label_entry('Event2',event2,i)

submit = partial(submit,uname, domain, event1, event2)

submit = Button(window,text='Submit',command=submit).grid(column=1,row=i+1)


window.mainloop()
