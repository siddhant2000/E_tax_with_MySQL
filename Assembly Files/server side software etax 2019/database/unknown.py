#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Apr 25, 2019 04:05:30 PM +0530  platform: Windows NT

import sys
import mysql.connector

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

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def delets(self):
        try :
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        except :
            tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
        
        mycursor=mydb.cursor()
        query = ("SELECT village, uidnumber, name FROM deleteddata")
        mycursor.execute(query)
        for(village, uidnumber, name) in mycursor:
            s="{}            {}          {}".format(village, uidnumber, name)
            self.box2o1.insert(0,s)

    def updates(self):
        try :
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='etax2019')
        except :
            tkinter.messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')
        
        mycursor=mydb.cursor()
        query = ("SELECT village,idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest FROM updateddata")
        mycursor.execute(query)
        for(village,idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest) in mycursor:
            s="{}        {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}       {}     {}     {}".format(village,idnumber, meternumber, wardnumber, name, housetax, healthtax, lighttax, watertax, total, reciptnumber, housetaxpaid, healthtaxpaid, lighttaxpaid, watertaxpaid, totalpaid, rest)
            self.box2o1.insert(0,s)
    def clears(self):
        self.box2o1.delete(0,tk.END)





    def exits(self):
        exit()
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1516x821+37+31")
        top.title("New Toplevel")
        top.configure(background="#ffff24")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.013, rely=0.024, height=81, width=156)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffff24")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Britannic Bold} -size 48 -weight bold")
        self.Label1.configure(foreground="#ff250d")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''eTAX''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.119, rely=0.024, height=81, width=156)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#ffff24")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Britannic Bold} -size 48 -weight bold")
        self.Label1_1.configure(foreground="#2212ff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''2019''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.073, rely=0.11, height=31, width=141)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffff24")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe Script} -size 12 -slant italic")
        self.Label2.configure(foreground="#13c12a")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''working for you''')

        self.backbutton = tk.Button(top)
        self.backbutton.place(relx=0.046, rely=0.171, height=44, width=97)
        self.backbutton.configure(activebackground="#ececec")
        self.backbutton.configure(activeforeground="#000000")
        self.backbutton.configure(background="#120bd8")
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
        self.backbutton.configure(foreground="#fcffff")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="black")
        self.backbutton.configure(pady="0")
        self.backbutton.configure(text='''Back''')

        self.exit = tk.Button(top)
        self.exit.place(relx=0.132, rely=0.171, height=44, width=97)
        self.exit.configure(activebackground="#ececec")
        self.exit.configure(activeforeground="#000000")
        self.exit.configure(background="#120bd8")
        self.exit.configure(disabledforeground="#a3a3a3")
        self.exit.configure(font="-family {Rockwell Extra Bold} -size 12 -weight bold")
        self.exit.configure(foreground="#fcffff")
        self.exit.configure(highlightbackground="#d9d9d9")
        self.exit.configure(highlightcolor="black")
        self.exit.configure(pady="0")
        self.exit.configure(text='''Exit''',command= self.exits)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.013, rely=0.962, height=21, width=56)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffff24")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''etax-2019''')

        self.Label3_3 = tk.Label(top)
        self.Label3_3.place(relx=0.013, rely=0.987, height=21, width=34)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#ffff24")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''v 1.0.2''')

        self.Label3_4 = tk.Label(top)
        self.Label3_4.place(relx=0.007, rely=1.035, height=21, width=134)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#ffff24")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(foreground="#000000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Working On Windows''')

        self.Label3_1 = tk.Label(top)
        self.Label3_1.place(relx=0.013, rely=1.011, height=21, width=164)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#ffff24")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Connected to MySQL server 8.0''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.277, rely=0.037, height=68, width=968)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffff24")
        self.Label4.configure(disabledforeground="#36911a")
        self.Label4.configure(font="-family {Rockwell Extra Bold} -size 40 -weight bold")
        self.Label4.configure(foreground="#36911a")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''DATA MODIFICATION REQUEST''')

        self.Label5_3 = tk.Label(top)
        self.Label5_3.place(relx=0.91, rely=0.95, height=28, width=172)
        self.Label5_3.configure(activebackground="#f9f9f9")
        self.Label5_3.configure(activeforeground="black")
        self.Label5_3.configure(background="#ffff24")
        self.Label5_3.configure(disabledforeground="#a3a3a3")
        self.Label5_3.configure(font="-family {Rockwell} -size 9")
        self.Label5_3.configure(foreground="#000000")
        self.Label5_3.configure(highlightbackground="#d9d9d9")
        self.Label5_3.configure(highlightcolor="black")
        self.Label5_3.configure(text='''Server  Status : Online''')

        self.Label5_4 = tk.Label(top)
        self.Label5_4.place(relx=0.917, rely=1.011, height=28, width=172)
        self.Label5_4.configure(activebackground="#f9f9f9")
        self.Label5_4.configure(activeforeground="black")
        self.Label5_4.configure(background="#ffff24")
        self.Label5_4.configure(disabledforeground="#a3a3a3")
        self.Label5_4.configure(font="-family {Rockwell} -size 9")
        self.Label5_4.configure(foreground="#000000")
        self.Label5_4.configure(highlightbackground="#d9d9d9")
        self.Label5_4.configure(highlightcolor="black")
        self.Label5_4.configure(text='''Host : localhost''')

        self.Label5_5 = tk.Label(top)
        self.Label5_5.place(relx=0.917, rely=1.035, height=28, width=172)
        self.Label5_5.configure(activebackground="#f9f9f9")
        self.Label5_5.configure(activeforeground="black")
        self.Label5_5.configure(background="#ffff24")
        self.Label5_5.configure(disabledforeground="#a3a3a3")
        self.Label5_5.configure(font="-family {Rockwell} -size 9")
        self.Label5_5.configure(foreground="#000000")
        self.Label5_5.configure(highlightbackground="#d9d9d9")
        self.Label5_5.configure(highlightcolor="black")
        self.Label5_5.configure(text='''Port : 3306''')

        self.box2o1 = ScrolledListBox(top)
        self.box2o1.place(relx=0.033, rely=0.268, relheight=0.652, relwidth=0.99)

        self.box2o1.configure(background="white")
        self.box2o1.configure(disabledforeground="#a3a3a3")
        self.box2o1.configure(font="TkFixedFont")
        self.box2o1.configure(foreground="black")
        self.box2o1.configure(highlightbackground="#d9d9d9")
        self.box2o1.configure(highlightcolor="#d9d9d9")
        self.box2o1.configure(selectbackground="#c4c4c4")
        self.box2o1.configure(selectforeground="black")
        self.box2o1.configure(width=10)

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.013, rely=0.146, relwidth=0.204)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.013, rely=0.244, relwidth=0.989)

        self.deleted = tk.Button(top)
        self.deleted.place(relx=0.343, rely=0.938, height=33, width=148)
        self.deleted.configure(activebackground="#ececec")
        self.deleted.configure(activeforeground="#000000")
        self.deleted.configure(background="#2020d8")
        self.deleted.configure(disabledforeground="#a3a3a3")
        self.deleted.configure(font="-family {Rockwell} -size 13 -weight bold")
        self.deleted.configure(foreground="#ffffff")
        self.deleted.configure(highlightbackground="#d9d9d9")
        self.deleted.configure(highlightcolor="black")
        self.deleted.configure(pady="0")
        self.deleted.configure(takefocus="0")
        self.deleted.configure(text='''Deleted Data''',command= self.delets)

        self.viewbutton_9 = tk.Button(top)
        self.viewbutton_9.place(relx=0.594, rely=0.938, height=33, width=108)
        self.viewbutton_9.configure(activebackground="#ececec")
        self.viewbutton_9.configure(activeforeground="#000000")
        self.viewbutton_9.configure(background="#2020d8")
        self.viewbutton_9.configure(disabledforeground="#a3a3a3")
        self.viewbutton_9.configure(font="-family {Rockwell} -size 13 -weight bold")
        self.viewbutton_9.configure(foreground="#ffffff")
        self.viewbutton_9.configure(highlightbackground="#d9d9d9")
        self.viewbutton_9.configure(highlightcolor="black")
        self.viewbutton_9.configure(pady="0")
        self.viewbutton_9.configure(takefocus="0")
        self.viewbutton_9.configure(text='''Clear all''',command= self.clears)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.viewbutton_1 = tk.Button(top)
        self.viewbutton_1.place(relx=0.475, rely=0.938, height=33, width=148)
        self.viewbutton_1.configure(activebackground="#ececec")
        self.viewbutton_1.configure(activeforeground="#000000")
        self.viewbutton_1.configure(background="#2020d8")
        self.viewbutton_1.configure(disabledforeground="#a3a3a3")
        self.viewbutton_1.configure(font="-family {Rockwell} -size 13 -weight bold")
        self.viewbutton_1.configure(foreground="#ffffff")
        self.viewbutton_1.configure(highlightbackground="#d9d9d9")
        self.viewbutton_1.configure(highlightcolor="black")
        self.viewbutton_1.configure(pady="0")
        self.viewbutton_1.configure(takefocus="0")
        self.viewbutton_1.configure(text='''Updated Data''',command= self.updates)

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=0.429, rely=0.122, height=81, width=516)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#ffff24")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font="-family {Britannic Bold} -size 48 -weight bold")
        self.Label1_2.configure(foreground="#ff250d")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''ADMINISTRATOR''')
        self.Label1_2.configure(width=516)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





