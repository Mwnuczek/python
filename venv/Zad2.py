# coding: utf-8
from tkinter import *
from threading import Thread
import time
from tkinter import messagebox


def show_entry_fields ():
    messagebox.showinfo( "Message ",'Dowolny komunikat ')

class Timer(Thread):
    over = False
    pause = False

    def __init__(self, func):
        Thread.__init__(self)
        self.func = func
        # self.setDaemon(True)

    def run(self):
        global t, root
        time.sleep(1)
        finish = False
        while not self.over and not finish:
            if not self.pause:
                finish = self.func()
            time.sleep(1)
        if finish:
            # root.focus_force()
            root.event_generate('<<pop>>', when='tail')
        t = None

    def kill(self):
        self.over = True

    def paus(self):
        self.pause = True

    def cont(self):
        self.pause = False


t = None
sec = None
root = Tk()
root.bind('<<pop>>', lambda event=None: show_entry_fields())
e1 = StringVar()
e2 = StringVar()


def show():
    global e1, e2, sec
    e1.set('%.2d' % (sec / 60))
    e2.set('%.2d' % (sec % 60))


def down():
    global sec
    if sec:
        sec -= 1;
        show()
        return False
    else:
        return True




def cd():
    global sec, t
    if t: t.cont();return
    sec = 0
    try:
        sec = int(e1.get()) * 60
    except Exception:
        pass
    try:
        sec += int(e2.get())
    except Exception:
        pass
    if not sec: return
    show()
    t = Timer(down)
    t.start()

    pass


def stp():
    global t, sec
    sec = 0;
    show()
    if t: t.kill()
    t = None


en1 = Entry(root, textvariable=e1, width=10, justify=RIGHT)
en2 = Entry(root, textvariable=e2, width=10)

stbtn = Button(root, width=10, text='start', command=cd)


stpbtn = Button(root, width=10, text='stop', command=stp)

en1.grid(row=0, column=0, )

en2.grid(row=0, column=1)
stbtn.grid(row=1, column=0)


stpbtn.grid(row=1, column=1)
root.geometry('+500+400')
root.mainloop()