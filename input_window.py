from tkinter import *
from tkinter import messagebox as msgb
from functools import partial
from sql_functions import sql_func

class input_win:
	def __init__(self):
		self.sq = sql_func()
		self.window = Tk()
		self.window.geometry('500x450')
		self.window.title('Employee Interest Input')

		self.uname = StringVar()
		self.domain = StringVar()
		self.event1 = StringVar()
		self.event2 = StringVar()

		self.new_win = None
		uname_label = Label(self.window,text='Name',height=3,width=10).grid(column=0,row=1)
		uname_entry = Entry(self.window,textvariable=self.uname,width=30).grid(column=1,row=1,padx=20)

		domain_label = Label(self.window,text='Domain').grid(column=0,row=2)
		self.domain.set('Artificial Intelligence')
		domain_drop = OptionMenu(self.window, self.domain, "Artificial Intelligence", "Blockchain", "C",\
		 "C++", "Cloud Computing", "Coding", "Data Science", "Development processes",\
		  "Finance", "Hardware", "Higher Education", "IoT", "Java", "JavaScript",\
		   "Machine learning", "Management", "Mobile Applications", "Networking",\
		    "Python", "Security", "Software Architecture", "Web Development", "Other")
		domain_drop.grid(column=1,row=2)

		event1_label = Label(self.window,text='Event1').grid(column=0,row=3)
		self.event1.set('Certifications')
		event1_drop = OptionMenu(self.window, self.event1, "Certifications", "Competitions", "Courses",\
		 "Expos", "Fests", "Hackathons", "Internships", "Jobs", "Seminars", "Talks",\
		  "Trainings", "Webinars", "Workshops")
		event1_drop.grid(column=1,row=3)

		event2_label = Label(self.window,text='Event2').grid(column=0,row=3)
		self.event2.set('Certifications')
		event2_drop = OptionMenu(self.window, self.event2, "Certifications", "Competitions", "Courses",\
		 "Expos", "Fests", "Hackathons", "Internships", "Jobs", "Seminars", "Talks",\
		  "Trainings", "Webinars", "Workshops")
		event2_drop.grid(column=1,row=4)

		submit = partial(self.submit,self.uname, self.domain, self.event1, self.event2)

		submit = Button(self.window,text='Submit',command=submit).grid(column=1,row=5)

		self.window.mainloop()

	def submit(self,uname,domain, event1, event2):
		self.sq.insert_data(uname.get(),domain.get(),event1.get(),event2.get())
		self.sq.close()

		MsgBox = msgb.askquestion('Submitted','Submitted and stored successfully',
									icon = 'warning')
		if MsgBox == 'yes':
			self.window.destroy()
			self.create_new_win()
			return

		else:
			messagebox.showinfo('Return','You will now return to the screen')

		return

	def create_new_win(self):
		self.new_win = Tk()
		self.new_win.geometry('500x450')

input_win()