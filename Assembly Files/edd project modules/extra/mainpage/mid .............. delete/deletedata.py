#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Apr 22, 2019 04:53:59 PM +0530  platform: Windows NT

import sys
import tkinter
from tkinter import messagebox
import mysql.connector
import time
import dbConnect
from dbConnect import DBConnect
import smtplib

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import deletedata_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    print ('prog_call = {}'.format(prog_call))
    prog_location = os.path.split(prog_call)[0]
    print ('prog_location = {}'.format(prog_location))
    sys.stdout.flush()
    root = tk.Tk()
    top = e_TAX_2019 (root)
    deletedata_support.init(root, top)
    root.mainloop()

w = None
def create_e_TAX_2019(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    print ('prog_call = {}'.format(prog_call))
    prog_location = os.path.split(prog_call)[0]
    print ('prog_location = {}'.format(prog_location))
    rt = root
    w = tk.Toplevel (root)
    top = e_TAX_2019 (w)
    deletedata_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_e_TAX_2019():
    global w
    w.destroy()
    w = None

class e_TAX_2019:
    def exits(self):
        msg=tkinter.messagebox.askyesno("e-TAX 2019","Do You Want To EXIT ?")
        if msg :
            exit()


    def backs(self):
        root.destroy()
        print("nwhcwjjwdj")


    def submit2(self):
        v=str(self.txt_villagename.get());
        n=str(self.txt_name.get());
        u=str(self.txt_uidnumber.get());

        t=str(time.asctime(time.localtime(time.time())))

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        mycursor=mydb.cursor()
        query=("INSERT INTO deleteddata (village, uidnumber, name)VALUES(%s,%s,%s)")
        datac=(v,u,n)
        mycursor.execute(query,datac)
        mydb.commit()

        totcontaint=str("Warning !!!!! \n\n New Request To Delete Entry \n\n Some Entries has been changed \n\n Here are the details : \n\n\n Village Name :"+v+"\n UID Number :"+u+"\n Name Of individual"+n+"\n Data deleted on :"+t)
        mail= smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('etaxsupp2019@gmail.com','Pass@123')
        mail.sendmail('etaxsupp2019@gmail.com','kulkarnipranesh1767@gmail.com',totcontaint)
        mail.close()
        messagebox.showinfo("e-TAX 2019","Successfully deleted The Entry")
        root.destroy()


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {Swatch it} -size 16"
        font13 = "-family {Segoe UI Black} -size 13 -weight bold"
        font14 = "-family {Shonar Bangla} -size 22"

        top.geometry("843x469+274+133")
        top.title("e-TAX 2019")
        top.configure(background="#727272")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.012, rely=0.021, relheight=0.309
                , relwidth=0.836)
        self.Frame1.configure(relief='ridge')
        self.Frame1.configure(borderwidth="10")
        self.Frame1.configure(relief='ridge')
        self.Frame1.configure(background="#595959")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=705)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.043, rely=0.207, height=59, width=196)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#595959")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Rockwell Extra} -size 40 -weight bold")
        self.Label1.configure(foreground="#0d4dff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''eTAX''')

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.298, rely=0.207, height=59, width=146)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#595959")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Rockwell Extra} -size 40 -weight bold")
        self.Label1_1.configure(foreground="#ff2b0a")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''2019''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.156, rely=0.621, height=31, width=184)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#595959")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Rage Italic} -size 19 -slant italic")
        self.Label2.configure(foreground="#f7ff0a")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''working for you''')

        self.Label1_2 = tk.Label(self.Frame1)
        self.Label1_2.place(relx=0.525, rely=0.207, height=69, width=306)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#595959")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font="-family {Rockwell Extra} -size 28 -weight bold")
        self.Label1_2.configure(foreground="#5faa14")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''delete DATA''')
        self.Label1_2.configure(width=306)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.107, rely=0.448, height=39, width=186)
        self.Label3.configure(background="#727272")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#f7ff1c")
        self.Label3.configure(text='''Village Name :''')
        self.Label3.configure(width=186)

        self.Label3_1 = tk.Label(top)
        self.Label3_1.place(relx=0.107, rely=0.554, height=29, width=186)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#727272")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Swatch it} -size 16")
        self.Label3_1.configure(foreground="#f7ff1c")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''UID Number :''')

        self.Label3_2 = tk.Label(top)
        self.Label3_2.place(relx=0.142, rely=0.64, height=39, width=116)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#727272")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font="-family {Swatch it} -size 16")
        self.Label3_2.configure(foreground="#f7ff1c")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Name  :''')
        self.Label3_2.configure(width=116)

        self.txt_villagename = tk.Entry(top)
        self.txt_villagename.place(relx=0.368, rely=0.469, height=20
                , relwidth=0.361)
        self.txt_villagename.configure(background="white")
        self.txt_villagename.configure(disabledforeground="#a3a3a3")
        self.txt_villagename.configure(font="TkFixedFont")
        self.txt_villagename.configure(foreground="#000000")
        self.txt_villagename.configure(insertbackground="black")
        self.txt_villagename.configure(width=304)

        self.txt_uidnumber = tk.Entry(top)
        self.txt_uidnumber.place(relx=0.368, rely=0.576, height=20
                , relwidth=0.361)
        self.txt_uidnumber.configure(background="white")
        self.txt_uidnumber.configure(disabledforeground="#a3a3a3")
        self.txt_uidnumber.configure(font="TkFixedFont")
        self.txt_uidnumber.configure(foreground="#000000")
        self.txt_uidnumber.configure(highlightbackground="#d9d9d9")
        self.txt_uidnumber.configure(highlightcolor="black")
        self.txt_uidnumber.configure(insertbackground="black")
        self.txt_uidnumber.configure(selectbackground="#c4c4c4")
        self.txt_uidnumber.configure(selectforeground="black")

        self.txt_name = tk.Entry(top)
        self.txt_name.place(relx=0.368, rely=0.661,height=20, relwidth=0.361)
        self.txt_name.configure(background="white")
        self.txt_name.configure(disabledforeground="#a3a3a3")
        self.txt_name.configure(font="TkFixedFont")
        self.txt_name.configure(foreground="#000000")
        self.txt_name.configure(highlightbackground="#d9d9d9")
        self.txt_name.configure(highlightcolor="black")
        self.txt_name.configure(insertbackground="black")
        self.txt_name.configure(selectbackground="#c4c4c4")
        self.txt_name.configure(selectforeground="black")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.771, rely=0.49, height=100, width=174)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(borderwidth="10")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"./delete1.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label4.configure(image=self._img0)
        self.Label4.configure(relief='raised')
        self.Label4.configure(text='''Label''')
        self.Label4.configure(width=174)

        self.btn_submit = tk.Button(top)
        self.btn_submit.place(relx=0.427, rely=0.832, height=54, width=194)
        self.btn_submit.configure(activebackground="#ececec")
        self.btn_submit.configure(activeforeground="#000000")
        self.btn_submit.configure(background="#3920d8")
        self.btn_submit.configure(borderwidth="10")
        self.btn_submit.configure(disabledforeground="#a3a3a3")
        self.btn_submit.configure(font=font13)
        self.btn_submit.configure(foreground="#ffffff")
        self.btn_submit.configure(highlightbackground="#d9d9d9")
        self.btn_submit.configure(highlightcolor="black")
        self.btn_submit.configure(pady="0")
        self.btn_submit.configure(text='''I Wish To Continue''',command = self.submit2)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.095, rely=0.725, height=43, width=560)
        self.Label5.configure(background="#727272")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font14)
        self.Label5.configure(foreground="#5bff3b")
        self.Label5.configure(text='''Disclaimer :  You Can Not recover the data once deleted''')

        self.btn_exit = tk.Button(top)
        self.btn_exit.place(relx=0.866, rely=0.192, height=44, width=104)
        self.btn_exit.configure(activebackground="#ececec")
        self.btn_exit.configure(activeforeground="#000000")
        self.btn_exit.configure(background="#ff3f0f")
        self.btn_exit.configure(borderwidth="10")
        self.btn_exit.configure(disabledforeground="#a3a3a3")
        self.btn_exit.configure(font="-family {Segoe UI Black} -size 13 -weight bold")
        self.btn_exit.configure(foreground="#ffffff")
        self.btn_exit.configure(highlightbackground="#d9d9d9")
        self.btn_exit.configure(highlightcolor="black")
        self.btn_exit.configure(pady="0")
        self.btn_exit.configure(text='''EXIT''',command = self.exits)
        self.btn_exit.configure(width=104)

        self.btn_back = tk.Button(top)
        self.btn_back.place(relx=0.866, rely=0.064, height=44, width=104)
        self.btn_back.configure(activebackground="#ececec")
        self.btn_back.configure(activeforeground="#000000")
        self.btn_back.configure(background="#3ba825")
        self.btn_back.configure(borderwidth="10")
        self.btn_back.configure(disabledforeground="#a3a3a3")
        self.btn_back.configure(font="-family {Segoe UI Black} -size 13 -weight bold")
        self.btn_back.configure(foreground="#ffffff")
        self.btn_back.configure(highlightbackground="#d9d9d9")
        self.btn_back.configure(highlightcolor="black")
        self.btn_back.configure(pady="0")
        self.btn_back.configure(text='''BACK''',command = self.backs)

if __name__ == '__main__':
    vp_start_gui()





