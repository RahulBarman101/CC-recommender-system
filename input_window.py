from tkinter import *
from functools import partial
from sql_functions import sql_func
import pickle

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

global new_win

def submit(uname,domain,event1,event2):
	''' 
	function for button press and store of data
	'''
	MsgBox = messagebox.askquestion ('Submitted','Submitted and stored successfully',
									icon = 'warning')
	if MsgBox == 'yes':
		window.destroy()
		create_new_win()
		return 
	else:
		messagebox.showinfo('Return','You will now return to the screen')
	sq.insert_data(uname.get(),domain.get(),event1.get(),event2.get())
	sq.close()
	return

def create_new_win():
	new_win = Tk()
	new_win.geometry('500x450')
	

uname_label = Label(window,text='Name',height=3,width=10).grid(column=0,row=1)
uname_entry = Entry(window,textvariable=uname,width=30).grid(column=1,row=1,padx=20)

domain_label = Label(window,text='Domain').grid(column=0,row=2)
domain.set('Artificial Intelligence')
domain_drop = OptionMenu(window, domain, "Artificial Intelligence", "Blockchain", "C",\
 "C++", "Cloud Computing", "Coding", "Data Science", "Development processes",\
  "Finance", "Hardware", "Higher Education", "IoT", "Java", "JavaScript",\
   "Machine learning", "Management", "Mobile Applications", "Networking",\
    "Python", "Security", "Software Architecture", "Web Development", "Other")
domain_drop.grid(column=1,row=2)

event1_label = Label(window,text='Event1').grid(column=0,row=3)
event1.set('Certifications')
event1_drop = OptionMenu(window, event1, "Certifications", "Competitions", "Courses",\
 "Expos", "Fests", "Hackathons", "Internships", "Jobs", "Seminars", "Talks",\
  "Trainings", "Webinars", "Workshops")
event1_drop.grid(column=1,row=3)

event2_label = Label(window,text='Event2').grid(column=0,row=3)
event2.set('Certifications')
event2_drop = OptionMenu(window, event2, "Certifications", "Competitions", "Courses",\
 "Expos", "Fests", "Hackathons", "Internships", "Jobs", "Seminars", "Talks",\
  "Trainings", "Webinars", "Workshops")
event2_drop.grid(column=1,row=4)

submit = partial(submit,uname, domain, event1, event2)

submit = Button(window,text='Submit',command=submit).grid(column=1,row=5)

window.mainloop()
