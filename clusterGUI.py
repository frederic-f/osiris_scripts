# https://www.python-course.eu/python_tkinter.php

import os
import wol

from tkinter import *

fields = 'Last Name', 'First Name', 'Job', 'Country'

hosts = 'horus', 'lenovo'

def fetch(entries):

    for entry in entries:

        field = entry[0]

        text  = entry[1].get()

        print('%s: "%s"' % (field, text))


def makeform(root, fields):

    entries = []

    for field in fields:

        row = Frame(root)

        lab = Label(row, width=15, text=field, anchor='w')

        ent = Entry(row)

        row.pack(side=TOP, fill=X, padx=5, pady=5)

        lab.pack(side=LEFT)

        ent.pack(side=RIGHT, expand=YES, fill=X)

        entries.append((field, ent))

    return entries


def listHosts(root, hosts):

    entries = []

    for host in hosts:

        row = Frame(root)

        lab1 = Label(row, width=15, text=host, anchor='w')

        # checkk if host is up
        HOST_UP = "Up" if os.system("ping -c 1 " + host) is 0 else "Down"

        lab2 = Label(row, width=15, text=HOST_UP, anchor='w')

        #ent = Entry(row)

        row.pack(side=TOP, fill=X, padx=5, pady=5)

        lab1.pack(side=LEFT)

        lab2.pack(side=RIGHT)

        #ent.pack(side=RIGHT, expand=YES, fill=X)

        #entries.append((host, ent))

    return True

def startNode(node):

    print("starting %s" % node)

    wol.wake_on_lan(node)


def startCluster():

    print("starting lenovo")

    wol.wake_on_lan("lenovo")

    print("starting horus")

    wol.wake_on_lan("horus")



if __name__ == '__main__':

    # init Tk
    root = Tk()

    # set window title
    root.wm_title("Cluster Manager")

    # Enter key
    root.bind('<Return>', (lambda event: startCluster()))

    # Esc key
    root.bind('<Escape>', (lambda event: root.quit()))

    ent = listHosts(root, hosts)

    #b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
    #b1.pack(side=LEFT, padx=5, pady=5)

    #b2 = Button(root, text='Quit', command=root.quit)
    #b2.pack(side=LEFT, padx=5, pady=5)

    row = Frame(root)

    b3 = Button(root, text='Start lenovo', command=(lambda: startNode("lenovo")))
    b3.pack(side=LEFT, padx=5, pady=5)

    b4 = Button(root, text='Start cluster', command=(lambda: startCluster()))
    b4.pack(side=LEFT, padx=5, pady=5)


    root.mainloop()