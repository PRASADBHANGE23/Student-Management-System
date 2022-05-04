from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
import pandas as pd
from tkinter.scrolledtext import*
import numpy as np
import matplotlib.pyplot as plt
import requests
import bs4
from sqlalchemy import *

try:
	wa="https://ipinfo.io/103.117.184.89?token=fd3458541faabc"
	res=requests.get(wa)
	data=res.json()
	city_name=data['city']
except Exception as e:
	showerror("issue")

"""

try:
	a1="http://api.openweathermap.org/data/2.5/weather/?units=metric"
	a2="&q= "+ city_name
	a3="&appid=" + "c6e315d09197cec231495138183954bd"
	wa=a1+a2+a3
	res=requests.get(wa)
	data=res.json()

	t=data['main']['temp']
except Exception as e:
	showerror("issue",e)

"""

try:
	wa="https://www.brainyquote.com/quote_of_the_day"
	res=requests.get(wa)
	data=bs4.BeautifulSoup(res.text,"html.parser")
	info=data.find("img",{"class":"p-qotd"})
	quote=info["alt"]
except Exception as e:
	showerror("issue")
	

def f1():
	add_window.deiconify()   
	main_window.withdraw()

def f2():
	main_window.deiconify()
	add_window.withdraw()

def f3():
	view_window.deiconify()
	main_window.withdraw()
	vw_st_data.delete(1.0,END)
	info=""
	con=None
	try:
		con=connect("project.db")
		cursor=con.cursor()
		sql="select*from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			info=info+"rno="+str(d[0])+"   name="+str(d[1])+"   marks="+str(d[2])+"\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("Issue",str(e))
	finally:
		if con is not None:
			con.close()

def f4():
	main_window.deiconify()
	view_window.withdraw()

def f5():
	con=None
	try:
		con=connect("project.db")
		cursor=con.cursor()
		sql="insert into student values('%d', '%s', '%d')"
		try:	
			rno = int(aw_ent_rno.get())
			rno != 0
		except ValueError:
			showerror("Rno Issue","Not accepted") 
			showerror("Rno Issue","Roll Number is empty")
			aw_ent_rno.delete(0, END)
			aw_ent_rno.focus()
			return	
		else:
			if (int(rno) == 0) or (int(rno) < 0):
				showerror("Rno Issue","Roll Number should be positive")
				aw_ent_rno.delete(0, END)
				aw_ent_rno.focus()
				return
		name = aw_ent_name.get()	
		len(name) != 0
		if len(name) == 0:
			showerror("Name Issue", "Name is empty")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return
		
	#Min Name Limit:

		if len(name) < 2:
			showerror("Name Issue","should enter more characters ")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return	
			
		if not name.isalpha() :
			showerror("Issue", "should enter a name in alphabate only")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return
		
	# Max Name Limit:
	
		len(name) == 15
		if len(name) > 15:
			showerror("Warning","Name limit exceeding ")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return
		try:
			marks = int(aw_ent_marks.get())
		except ValueError:
			showerror("Issue","Not accepted")
			showerror("Issue","Marks are empty")
			aw_ent_marks.delete(0, END)
			aw_ent_marks.focus()
			return
	
		else:
			if ((int(marks) < 0) or (int(marks) > 100)):
				showerror("Marks Issue", "should enter maks in between 0-100")
				aw_ent_marks.delete(0, END)
				aw_ent_marks.focus()
				return
	
		cursor.execute(sql % (rno,name,marks))
		data=cursor.fetchall()
		con.commit()
		showinfo("success","record added")
		aw_ent_rno.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_marks.delete(0,END)
		aw_ent_rno.focus()
	except Exception as e:
		con.rollback()
		showerror("issue","Roll no already exist")
		aw_ent_rno.delete(0,END)
		aw_ent_rno.focus()
	finally:
		if con is not None:
			con.close()

def f6():
	main_window.deiconify()
	update_window.withdraw()

def f7():
	con = None
	try:
		con = connect("project.db")
		cursor = con.cursor()
		sql = "update student set name = '%s', marks = '%d' where rno = '%d' "
		try:
			rno = int(uw_ent_rno.get())
			rno != 0
		except ValueError:
			showerror("Rno Issue","Not accepted")
			showerror("Rno Issue","Roll number is empty")
			uw_ent_rno.delete(0, END)
			uw_ent_rno.focus()
			return
		else:
			if (int(rno) == 0) or (int(rno) < 0):
				showerror("Rno Issue", "Roll number should be positive")
				uw_ent_rno.delete(0, END)
				uw_ent_rno.focus()
				return
		
		name = uw_ent_name.get()
		len(name) != 0
		if len(name) == 0:
			showerror("Name Empty","name should not be empty ")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return
		if len(name) < 2:
			showerror("Short Name Issue","enter more character")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return
		
		if not name.isalpha() :
			showerror("Name Issue", "Not accepted Name")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return	

		len(name) == 15
		if len(name) > 15:
			showerror("Warning !", "Name limit exceeding")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return

		
		try:
			marks = int(uw_ent_marks.get())
		except ValueError:
			showerror("Issue","Not accepted Marks")
			showerror("Issue","marks is empty ")
			uw_ent_marks.delete(0, END)
			uw_ent_marks.focus()
			return

		else:	
			if ((int(marks) == 0) or (int(marks) < 0) or (int(marks) > 100)):
				showerror(" Issue", "marks should be in between 0-100 ")
				uw_ent_marks.delete(0, END)
				uw_ent_marks.focus()
				return
		
		cursor.execute(sql%(name, marks, rno))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success ","Record Updated ")
		else:
			showerror("Failed", "Record does not exists !")
		uw_ent_rno.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_marks.delete(0, END)
		uw_ent_rno.focus()
		return
		uw_ent_rno.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_marks.delete(0,END)
		uw_ent_rno.focus()
	except Exception as e:
		con.rollback()
		#showerror("issue","roll number already exist")
	finally:
		if con is not None:
			con.close()

def f8():
	update_window.deiconify()   
	main_window.withdraw()

def f9():
	main_window.deiconify()
	delete_window.withdraw()

def f10():
	con=None
	try:
		con=connect("project.db")
		cursor=con.cursor()
		sql="delete from student where rno='%s' "
		try:	
			rno = int(dw_ent_rno.get())
			rno != 0
		except ValueError:
			showerror("Rno Issue","Not accepted") 
			showerror("Rno Issue","Roll Number is empty")
			dw_ent_rno.delete(0, END)
			dw_ent_rno.focus()
			return	
		else:
			if (int(rno) == 0) or (int(rno) < 0):
				showerror("Rno Issue","Roll Number should be positive")
				dw_ent_rno.delete(0, END)
				dw_ent_rno.focus()
				return
		cursor.execute(sql % (rno))
		if cursor.rowcount==1:
			con.commit()
			showinfo("success","Roll number,data deleted")
			dw_ent_rno.delete(0,END)
			dw_ent_rno.focus()
		else:
			showerror("failure","Roll number does not exist")
		
	except Exception as e:
		con.rollback()
		
	finally:	
		if con is not None:
			con.close()

def f11():
	delete_window.deiconify()   
	main_window.withdraw()

def f12():	
	c1=create_engine('sqlite:///project.db').connect()
	data=pd.read_sql_table('student',c1)
	print(data)
	name=data['name'].tolist()
	marks=data['marks'].tolist()	
	plt.bar(name,marks,color=["orange","green","blue","red","yellow"])
	plt.title("Batch Information")
	plt.xlabel("Name")
	plt.ylabel("Marks")
	plt.show()
		
	
	
main_window=Tk()
main_window.title("S.M.S")
main_window.geometry("500x500+400+100")
main_window.configure(bg="PaleGreen3")

f=("Times New Roman",20,"bold")
mw_btn_add=Button(main_window,text="ADD",font=f,width=11,command=f1)
mw_btn_view=Button(main_window,text="VIEW",font=f,width=11,command=f3)
mw_btn_update=Button(main_window,text="UPDATE",font=f,width=11,command=f8)
mw_btn_delete=Button(main_window,text="DELETE",font=f,width=11,command=f11)
mw_btn_charts=Button(main_window,text="CHARTS",font=f,width=11,command=f12)
mw_btn_add.pack(pady=10)
mw_btn_view.pack(pady=10)
mw_btn_update.pack(pady=10)
mw_btn_delete.pack(pady=10)
mw_btn_charts.pack(pady=10)

mw_lbl_location=Label(main_window,text="Location:"+city_name,font=f)
mw_lbl_location.place(x=10,y=380)

# mw_lbl_temp=Label(main_window,text="Temp:"+str(t),font=f)
# mw_lbl_temp.place(x=330,y=380)
mw_lbl_qotd=Label(main_window,text="QOTD:"+quote,font=f)
mw_lbl_qotd.place(x=10,y=430)

add_window=Toplevel(main_window) 
add_window.title("Add St.")
add_window.geometry("500x500+400+100")
add_window.configure(bg="SlateGray3")

aw_lbl_rno=Label(add_window,text="enter rno:",font=f)
aw_ent_rno=Entry(add_window,bd=5,font=f)
aw_lbl_name=Label(add_window,text="enter name:",font=f)
aw_ent_name=Entry(add_window,bd=5,font=f)
aw_lbl_marks=Label(add_window,text="enter marks:",font=f)
aw_ent_marks=Entry(add_window,bd=5,font=f)
aw_btn_save=Button(add_window,text="Save",font=f,command=f5)
aw_btn_back=Button(add_window,text="Back",font=f,command=f2)
aw_lbl_rno.pack(pady=10)
aw_ent_rno.pack(pady=10)
aw_lbl_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lbl_marks.pack(pady=10)
aw_ent_marks.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
add_window.withdraw()

view_window=Toplevel(main_window)
view_window.title("Veiw st.")
view_window.geometry("500x500+400+100")
view_window.configure(bg="khaki3")
vw_st_data=ScrolledText(view_window,width=30,height=10,font=f)
vw_btn_back=Button(view_window,text="Back",font=f,command=f4)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
view_window.withdraw()

update_window=Toplevel(main_window) 
update_window.title("Update St.")
update_window.geometry("500x500+400+100")
update_window.configure(bg="burlywood3")

uw_lbl_rno=Label(update_window,text="enter rno:",font=f)
uw_ent_rno=Entry(update_window,bd=5,font=f)
uw_lbl_name=Label(update_window,text="enter name:",font=f)
uw_ent_name=Entry(update_window,bd=5,font=f)
uw_lbl_marks=Label(update_window,text="enter marks:",font=f)
uw_ent_marks=Entry(update_window,bd=5,font=f)
uw_btn_save=Button(update_window,text="Save",font=f,command=f7)
uw_btn_back=Button(update_window,text="Back",font=f,command=f6)
uw_lbl_rno.pack(pady=10)
uw_ent_rno.pack(pady=10)
uw_lbl_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lbl_marks.pack(pady=10)
uw_ent_marks.pack(pady=10)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)
update_window.withdraw()

delete_window=Toplevel(main_window) 
delete_window.title("Delete St.")
delete_window.geometry("500x500+400+100")
delete_window.configure(bg="LightSkyBlue3")

dw_lbl_rno=Label(delete_window,text="enter rno:",font=f)
dw_ent_rno=Entry(delete_window,bd=5,font=f)
dw_btn_save=Button(delete_window,text="Save",font=f,command=f10)
dw_btn_back=Button(delete_window,text="Back",font=f,command=f9)
dw_lbl_rno.pack(pady=10)
dw_ent_rno.pack(pady=10)
dw_btn_save.pack(pady=10)
dw_btn_back.pack(pady=10)
delete_window.withdraw()







main_window.mainloop()