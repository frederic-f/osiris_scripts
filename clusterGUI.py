#!/usr/bin/python3.5

import os
import wol
import subprocess
from pexpect import pxssh
import getpass

#from subprocess import run
#call(["ls", "-l"])

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


def stopCluster():

    stopNode("lenovo")

    stopNode("horus")




def stopNode(node):

    global password
    if password == "":
        password = getpass.getpass()


    if node == "lenovo":
        #from subprocess import run

        subprocess.run(["net", "rpc", "shutdown", "-I", "192.168.1.95", "-U", "pv1%{}".format(password)])



    if node == "horus":
        print("stopping horus...")
        s = pxssh.pxssh()

        host = "horus"
        user = "pv1"
        #password = input('Enter password for pv1@horus: ')


        if not s.login(host, user, password):
            print("SSH session failed on login.")
            print(str(s))
        else:
            print("SSH session login successful")
            print("sending ")
            s.sendline('sudo shutdown now')
            s.expect('.*')
            #print(s.before)
            #print(s.after)
            s.sendline(password)
            s.prompt()  # match the prompt
            #print(s.before)  # print everything before the prompt.
            s.logout()


if __name__ == '__main__':

    password = ""

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

    b4= Button(root, text='Stop lenovo', command=(lambda: stopNode("lenovo")))
    b4.pack(side=LEFT, padx=5, pady=5)

    b5 = Button(root, text='Start cluster', command=(lambda: startCluster()))
    b5.pack(side=LEFT, padx=5, pady=5)

    b6= Button(root, text='Stop Cluster', command=(lambda: stopCluster()))
    b6.pack(side=LEFT, padx=5, pady=5)


    root.mainloop()