import MySQLdb
import tkinter as tk
import random
from tkinter import messagebox
global count
count=3
def generate_id():
    global count;
    k=random.randint(101,999)
    x=ent1.get()
    messagebox.showinfo('registered',k)
    connect=MySQLdb.connect(host='localhost',user='root',password='',database='inquizitive')
    cur=connect.cursor()
    cur.execute(""" INSERT INTO quiz_participant(pid,Name,loginid) values(%s,%s,%s)""",(count,x,k))
    count+=1
    connect.commit()
    connect.close()


root=tk.Tk()
root.geometry('350x100')
root.title('registration')
frame=tk.Frame(root)
lab=tk.Label(frame,text='Enter  name:   ',font='verdena 20 italic')
ent1=tk.Entry(frame,width=30)
lab.pack(side='left')
ent1.pack(side='right')
frame.pack(side='top')
but1=tk.Button(root,text='register',width=5,command=generate_id,bg='green',font='times 15 italic')
but1.pack(side='bottom')
root.mainloop()
