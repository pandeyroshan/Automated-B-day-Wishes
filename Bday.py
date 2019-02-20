from tkinter import *
import smtplib
from datetime import datetime
import sqlite3
import tkinter.messagebox
from tkinter import messagebox
root = Tk()
root.geometry('500x200')
root.title('MAIN WINDOW')
root.configure(background='#222022')
def insertDOB():
	insertRoot = Tk()
	insertRoot.geometry('500x270')
	insertRoot.configure(background='#222022')
	def insertData():
		name = e1.get()
		dob = e2.get()
		email = e3.get()
		date = dob[:2]
		month = dob[3:5]
		year = dob[-4:]
		con=sqlite3.Connection('bday')
		cur=con.cursor()
		cur.execute("create table if not exists newdataTable2(name varchar(30),date varchar(3),month varchar(3),year varchar(3),email varchar(30))")
		cur.execute("insert into newdataTable2 values(?,?,?,?,?)",(name,date,month,year,email))
		cur.execute('select * from newdataTable2')
		a = cur.fetchall()
		print (a)
		con.commit()
		text = name+" has been added to your friend list."
		messagebox.showinfo("STATUS", text)
	def resetData():
		e1.delete(0,END)
		e2.delete(0,END)
	Label(insertRoot,text='ADD FRIEND',width=34,font='Arial 20 bold',bg='#222022',fg='#6ead3a').grid(row=0,column=0,columnspan=2)
	Label(insertRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=1,column=0)
	Label(insertRoot,text="Name :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=2,column=0)
	e1 = Entry(insertRoot,bd=3,width=17,bg='#222022',fg='#ffffff',font='Arial 15')
	e1.grid(row=2,column=1)
	Label(insertRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=3,column=0)
	Label(insertRoot,text="Date :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=4,column=0)
	e2 = Entry(insertRoot,bd=3,width=17,bg='#222022',fg='#ffffff',font='Arial 15')
	e2.grid(row=4,column=1)
	Label(insertRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=5,column=0)
	Label(insertRoot,text="Email :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=6,column=0)
	e3 = Entry(insertRoot,bd=3,width=17,bg='#222022',fg='#ffffff',font='Arial 15')
	e3.grid(row=6,column=1)
	Label(insertRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=7,column=0)
	Button(insertRoot,text="RESET",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=resetData).grid(row=8,column=0)
	Button(insertRoot,text="INSERT",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=insertData).grid(row=8,column=1)
	insertRoot.mainloop()
def deleteDOB():
	deleteRoot = Tk()
	deleteRoot.geometry('500x180')
	deleteRoot.configure(background='#222022')
	def deleteData():
		name = e1.get()
		con=sqlite3.Connection('bday')
		cur=con.cursor()
		sqlText = 'delete from newdataTable2 where name = "'+name+'"'
		cur.execute(sqlText)
		con.commit()
		text= name+' has been removed from your friend List.'
		messagebox.showinfo("STATUS", text)
	def resetData():
		e1.delete(0,END)
	Label(deleteRoot,text='REMOVE FRIEND',width=34,font='Arial 20 bold',bg='#222022',fg='#6ead3a').grid(row=0,column=0,columnspan=2)
	Label(deleteRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=1,column=0)
	Label(deleteRoot,text="NAME :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=2,column=0)
	e1 = Entry(deleteRoot,bd=3,width=17,bg='#222022',fg='#ffffff',font='Arial 15')
	e1.grid(row=2,column=1)
	Label(deleteRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=3,column=0)
	Label(deleteRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=4,column=0)
	Button(deleteRoot,text="RESET",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=resetData).grid(row=5,column=0)
	Button(deleteRoot,text="REMOVE",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=deleteData).grid(row=5,column=1)
	deleteRoot.mainloop()
def checkDOB():
	checkRoot = Tk()
	checkRoot.geometry('500x220')
	checkRoot.configure(background='#222022')
	def checkData():
		name = e1.get()
		con=sqlite3.Connection('bday')
		cur=con.cursor()
		sqlText='select date,month,year from newdataTable2 where name = "'+name+'"'
		cur.execute(sqlText)
		a = cur.fetchall()
		data = str(a[0][0])+"-"+str(a[0][1])+"-"+str(a[0][2])
		e2.insert(0,data)
		con.commit()
	def resetData():
		e1.delete(0,END)
		e2.delete(0,END)
	Label(checkRoot,text="CHECK B'DAY",width=34,font='Arial 20 bold',bg='#222022',fg='#6ead3a').grid(row=0,column=0,columnspan=2)
	Label(checkRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=1,column=0)
	Label(checkRoot,text="NAME :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=2,column=0)
	e1 = Entry(checkRoot,bd=3,width=17,bg='#222022',fg='#ffffff',font='Arial 15')
	e1.grid(row=2,column=1)
	Label(checkRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=3,column=0)
	Label(checkRoot,text="DATE :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=4,column=0)
	e2 = Entry(checkRoot,bd=3,width=17,bg='#222022',fg='#ffffff',font='Arial 15')
	e2.grid(row=4,column=1)
	Label(checkRoot,text="",bg='#222022',width=10,font='Arial 12').grid(row=5,column=0)
	Button(checkRoot,text="RESET",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=resetData).grid(row=6,column=0)
	Button(checkRoot,text="CHECK",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=checkData).grid(row=6,column=1)
	checkRoot.mainloop()
def refreshWish():
	dateTime= str(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
	date = dateTime[:2]
	month = dateTime[3:5]
	con=sqlite3.Connection('bday')
	cur=con.cursor()
	sqlText='select email from newdataTable2 where date ="'+date+'" AND month = "'+month+'"'
	cur.execute(sqlText)
	a = cur.fetchall()
	for data in a:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("pandeyroshan556@gmail.com", "your_password_here")
		message = 'Subject: {}\n\n{}'.format("Happy Birthday", "Happy B'day to you.")
		server.sendmail("pandeyroshan556@gmail.com", data[0], "Happy B'day to you")
		server.quit()
	messagebox.showinfo("STATUS", "Mails has been sent to all your Friends.")
Label(root,text='AUTOMATED BIRTHDAY WISHES',width=34,font='Arial 20 bold',bg='#222022',fg='#6ead3a').grid(row=0,column=0,columnspan=2)
Label(root,text="",bg='#222022',width=10,font='Arial 12').grid(row=1,column=0)
Button(root,text="INSERT",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=insertDOB).grid(row=2,column=0)
Button(root,text="DELETE",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=deleteDOB).grid(row=2,column=1)
Label(root,text="",bg='#222022',width=10,font='Arial 12').grid(row=3,column=0)
Button(root,text="CHECK",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=checkDOB).grid(row=4,column=0)
Button(root,text="REFRESH",borderwidth=3,bg='#1ed2f4',width=10,font='Arial 12',command=refreshWish).grid(row=4,column=1)
root.mainloop()