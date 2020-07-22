from tkinter import *
from recommend import recommend
from functools import partial
import pandas as pd
from datetime import date

rec = recommend()
class predict_window:
	def __init__(self):
		self.window = Tk()
		self.window.geometry('500x450')
		self.window.title('Predict self.window')
		self.event = StringVar()
		self.num = StringVar()
		self.df = pd.read_csv('CCMLEmployeeData.csv')

		main_label = Label(self.window,text='event',height=3,width=10).grid(column=0,row=1)
		main_text = Entry(self.window,textvariable=self.event).grid(column=1,row=1)
		num_pep = Label(self.window,text='How many people to select').grid(column=0,row=2)
		num_text = Entry(self.window,textvariable=self.num).grid(column=1,row=2)
		generate = partial(self.generate,self.event,self.num)
		get = Button(self.window,text='get record',command=generate).grid(column=1,row=3)
		self.window.mainloop()

	def generate(self,s,n=1):
		s = s.get()
		n = n.get()
		n = int(n)
		r = rec.predict(s,n)
		r = r[1:n+1]
		x = []
		for i in r:
			z = i[0]
			x.append(self.df['Name'].iloc[z])
		new_df = pd.DataFrame()
		new_df['Name'] = x
		new_df.to_csv(f'{rec.dom}_event_{date.today()}.csv')



predict_window()
