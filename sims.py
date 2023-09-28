
from tkinter import *
from tkinter import ttk
import pymysql


class StudentsInfo:
    def __init__(self ,root):
        self.root = root
        self.root.geometry('1500x800')
        self.root.title('SIMS')
        title1 = Label(self.root, text='Student Information Management System',
                       font=('Cooper Black', 35, 'bold'), bg='orange', fg='white')
        title1.pack(fill='x')


        self.firstnameVar = StringVar()
        self.lastnameVar = StringVar()
        self.rollnoVar = StringVar()
        self.emailidVar = StringVar()
        self.contactVar = StringVar()
        self.courseVar = StringVar()
        self.locationVar = StringVar()


        # Creating Frames
        dataEntryFrame = Frame(self.root, bg='cadet blue')
        dataEntryFrame.place(x=4, y=70, width=500, height=700)

        dataDisplayFrame = Frame(self.root, bg='cadet blue')
        dataDisplayFrame.place(x=520, y=70, width=1000, height=700)

        # Working With DataEntryFrame
        title2 = Label(dataEntryFrame, text='Students Entry...',
                       font=('Cooper Black', 25, 'bold'), bg='green', fg='white')
        title2.grid(row=0, columnspan=2, padx=80, pady=20)
        # First name
        fnameLb1 = Label(dataEntryFrame, text='First name: ', font=('Comic Sans MS', 15, 'bold'), bg='green',
                         fg='white')
        fnameLb1.grid(row=1, column=0, sticky='W')
        # fname entry
        fnameentry = Entry(dataEntryFrame, textvariable=self.firstnameVar, font=('Book Antiqua', 20, 'bold'))
        fnameentry.grid(row=1, column=1, sticky='E', pady=10)

        # Last name
        lnameLb1 = Label(dataEntryFrame, text='Last name: ', font=('Comic Sans MS', 15, 'bold'), bg='green', fg='white')
        lnameLb1.grid(row=2, column=0, sticky='W')
        # lname entry
        lnameentry = Entry(dataEntryFrame, textvariable=self.lastnameVar, font=('Book Antiqua', 20, 'bold'))
        lnameentry.grid(row=2, column=1, sticky='E', pady=10)

        # Rollno
        rollnoLb1 = Label(dataEntryFrame, text='Roll No: ', font=('Comic Sans MS', 15, 'bold'), bg='green', fg='white')
        rollnoLb1.grid(row=3, column=0, sticky='W')
        # Roll no entry
        rollentry = Entry(dataEntryFrame, textvariable=self.rollnoVar, font=('Book Antiqua', 20, 'bold'))
        rollentry.grid(row=3, column=1, sticky='E', pady=10)

        # Email
        emailidLb1 = Label(dataEntryFrame, text='Email Id: ', font=('Comic Sans MS', 15, 'bold'), bg='green',
                           fg='white')
        emailidLb1.grid(row=4, column=0, sticky='W')
        # Email entry
        emailentry = Entry(dataEntryFrame,textvariable=self.emailidVar, font=('Book Antiqua', 20, 'bold'))
        emailentry.grid(row=4, column=1, sticky='E', pady=10)

        # Contact No
        contactLb1 = Label(dataEntryFrame, text='Contact No: ', font=('Comic Sans MS', 15, 'bold'), bg='green',
                           fg='white')
        contactLb1.grid(row=5, column=0, sticky='W')
        # Contact No entry
        contactentry = Entry(dataEntryFrame, textvariable=self.contactVar, font=('Book Antiqua', 20, 'bold'))
        contactentry.grid(row=5, column=1, sticky='E', pady=10)

        # Course
        courseLb1 = Label(dataEntryFrame, text='Course:', font=('Comic Sans MS', 15, 'bold'), bg='green', fg='white')
        courseLb1.grid(row=6, column=0, sticky='W')
        # Course entry
        courseentry = Entry(dataEntryFrame, textvariable=self.courseVar, font=('Book Antiqua', 20, 'bold'))
        courseentry.grid(row=6, column=1, sticky='E', pady=10)

        # Location
        locationLb1 = Label(dataEntryFrame, text='Location: ', font=('Comic Sans MS', 15, 'bold'), bg='green',
                            fg='white')
        locationLb1.grid(row=7, column=0, sticky='W')
        # Location entry
        locationentry = Entry(dataEntryFrame, textvariable=self.locationVar, font=('Book Antiqua', 20, 'bold'))
        locationentry.grid(row=7, column=1, sticky='E', pady=10)

        # Creating Frame For Button
        btnFrame = Frame(dataEntryFrame, bg='green', border=4, relief=RAISED)
        btnFrame.place(x=10, y=500, width=480, height=150)

        # Add Button
        addbtn = Button(btnFrame, text='Add',command= self.adding,font=('Book Antiqua', 20, 'bold'), bg='red', fg='yellow')
        addbtn.grid(row=0, column=0, padx=8, pady=45)

        # Update Button
        updatebtn = Button(btnFrame, text='Update',command=self.updating, font=('Book Antiqua', 20, 'bold'), bg='red', fg='yellow')
        updatebtn.grid(row=0, column=1, padx=8, pady=45)

        # Delete Button
        deletebtn = Button(btnFrame, text='Delete',command=self.deleting, font=('Book Antiqua', 20, 'bold'), bg='red', fg='yellow')
        deletebtn.grid(row=0, column=2, padx=8, pady=45)
       # Clear Button
        clearbtn = Button(btnFrame,command=self.clearing, text='Clear', font=('Book Antiqua', 20, 'bold'), bg='red', fg='yellow')
        clearbtn.grid(row=0, column=3, padx=8, pady=45)


        # Working With Data dataDisplayFrame

        title3 = Label(dataDisplayFrame, text='Data Display Here...',
                   font=('Cooper Black', 25, 'bold'), bg='green', fg='white')
        title3.place(x=300, y=20)
        tableFrame=Frame(dataDisplayFrame, width=970, height=560, bg= 'green', bd=5, relief=RAISED)
        tableFrame.place(x=10, y=93)
        #ttk imported
        self.StudentsData = ttk.Treeview(tableFrame, columns=('first_name','last_name','roll_no','emailid','contact','course','location'))
        self.StudentsData.heading('first_name', text='First Name')
        self.StudentsData.heading('last_name', text='Last Name')
        self.StudentsData.heading('roll_no', text='Roll No')
        self.StudentsData.heading('emailid', text='Email Id')
        self.StudentsData.heading('contact', text='Contact No')
        self.StudentsData.heading('course', text='Course')
        self.StudentsData.heading('location', text='Location')
        #Display table data
        self.StudentsData['show'] = 'headings'
        self.StudentsData.column('first_name', width=150, anchor='center')
        self.StudentsData.column('last_name', width=150, anchor='center')
        self.StudentsData.column('roll_no', width=100, anchor='center')
        self.StudentsData.column('emailid', width=200, anchor='center')
        self.StudentsData.column('contact', width=100, anchor='center')
        self.StudentsData.column('course', width=150, anchor='center')
        self.StudentsData.column('location', width=100, anchor='center')

        self.StudentsData.pack()

        self.fetching()
        self.StudentsData.bind('<ButtonRelease-1>', self.get_cursor)



    # adding command
    def adding(self):
        connection = pymysql.Connect(host='localhost', user='root', password='Rmanas06@',db= 'studentinfo')
        c=connection.cursor()
        c.execute('insert into studentsdata values(%s,%s,%s,%s,%s,%s,%s)',
                ( self.firstnameVar.get(),
                self.lastnameVar.get(),
                self.rollnoVar.get(),
                self.emailidVar.get(),
                self.contactVar.get(),
                self.courseVar.get(),
                self.locationVar.get()

                ))
        connection.commit()
        self.fetching()
        self.clearing()
        connection.close()

        # Clearing command
    def clearing(self):
        self.rollnoVar.set(''),
        self.firstnameVar.set(''),
        self.lastnameVar.set(''),
        self.emailidVar.set(''),
        self.contactVar.set(''),
        self.courseVar.set(''),
        self.locationVar.set('')
    def fetching(self):
        connection = pymysql.Connect(host='localhost', user='root', password='Rmanas06@',db= 'studentinfo')
        c=connection.cursor()
        c.execute('select * from studentsdata')
        data= c.fetchall()
        self.StudentsData.delete(*self.StudentsData.get_children())
        for i in data:
            self.StudentsData.insert('', END, values=i)
        connection.commit()
        connection.close()
    def get_cursor(self,var):
        cursor_row = self.StudentsData.focus()
        content = self.StudentsData.item(cursor_row)
        row=content['values']

        self.firstnameVar.set(row[0])
        self.lastnameVar.set(row[1])
        self.rollnoVar.set(row[2])
        self.emailidVar.set(row[3])
        self.contactVar.set(row[4])
        self.courseVar.set(row[5])
        self.locationVar.set(row[6])
    # updating command
    def updating(self):
        connection = pymysql.Connect(host='localhost', user='root', password='Rmanas06@',db= 'studentinfo')
        c=connection.cursor()
        c.execute('update StudentsData set firstname=%s,last_name=%s,email_id=%s,contact=%s,course=%s,location=%s where id=%s',
                (
                self.firstnameVar.get(),
                self.lastnameVar.get(),
                self.emailidVar.get(),
                self.contactVar.get(),
                self.courseVar.get(),
                self.locationVar.get(),
                self.rollnoVar.get()

                ))
        connection.commit()
        self.fetching()
        self.clearing()
        connection.close()

    #Deletting Command
    def deleting(self):
        connection = pymysql.Connect(host='localhost', user='root', password='Rmanas06@', db='studentinfo')
        c = connection.cursor()
        c.execute('delete from StudentsData where id=%s', self.rollnoVar.get())
        connection.commit()
        connection.close()
        self.fetching()
        self.clearing()

root = Tk()
obj = StudentsInfo(root)
root.mainloop()
