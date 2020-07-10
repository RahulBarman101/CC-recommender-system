from tkinter import *
import sqlite3

window = Tk()
window.title('Employee Preferences Window')
window.geometry("400x400")

#Create Table
'''
c.execute("""CREATE TABLE preferences (
        employee_name text,
        domain_preference text,
        event1_preference text,
        event2_preference text
        )""")
'''
def open():
    top = Toplevel()
    top.title('Successful Submission')
    top.geometry("400x400")
    lbl = Label(top, text="**Thank you for giving your preferences!**").pack()
    btn = Button(top, text = "Exit", command = top.destroy).pack()

click = Button(window, text = "Click here after submitting", command = open)
click.grid(row = 9, column = 1, columnspan = 2, pady = 10, padx = 10)

# Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('employee_preferences.db')
    # Create cursor
    c = conn.cursor()
    #Insert into table
    c.execute("INSERT INTO preferences VALUES(:name, :domain, :event1, :event2)",
              {
                  'name': name.get(),
                  'domain': domain.get(),
                  'event1': event1.get(),
                  'event2': event2.get()
              })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    #Clear the text boxes
    name.delete(0, END)


#Create text boxes
name = Entry(window, width = 30)
name.grid(row = 0, column = 1, padx = 20)

#Create drop boxes
domain = StringVar()
domain.set("Artificial Intelligence")
drop = OptionMenu(window, domain, "Artificial Intelligence", "Blockchain", "C", "C++", "Cloud Computing", "Coding", "Data Science", "Development processes", "Finance", "Hardware", "Higher Education", "IoT", "Java", "JavaScript", "Machine learning", "Management", "Mobile Applications", "Networking", "Python", "Security", "Software Architecture", "Web Development", "Other")
drop.grid(row = 1, column = 1)
event1 = StringVar()
event1.set("Certifications")
drop1 = OptionMenu(window, event1, "Certifications", "Competitions", "Courses", "Expos", "Fests", "Hackathons", "Internships", "Jobs", "Seminars", "Talks", "Trainings", "Webinars", "Workshops")
drop1.grid(row = 2, column = 1)
event2 = StringVar()
event2.set("Certifications")
drop2 = OptionMenu(window, event2, "Certifications", "Competitions", "Courses", "Expos", "Fests", "Hackathons", "Internships", "Jobs", "Seminars", "Talks", "Trainings", "Webinars", "Workshops")
drop2.grid(row = 3, column = 1)

#Create text box labels
name_label = Label(window, text = "Employee name")
name_label.grid(row = 0, column = 0)

domain_label = Label(window, text = "Domain preference")
domain_label.grid(row = 1, column = 0)

event1_label = Label(window, text = "Event1 preference")
event1_label.grid(row = 2, column = 0)

event2_label = Label(window, text = "Event2 preference")
event2_label.grid(row = 3, column = 0)

# Create a submit button
submit = Button(window, text = "Submit", command = submit)
submit.grid(row = 8, column = 1, columnspan = 2, pady = 10, padx = 10)


window.mainloop()