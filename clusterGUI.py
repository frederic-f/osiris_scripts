# https://www.python-course.eu/python_tkinter.php

import wol

from tkinter import *
fields = 'Last Name', 'First Name', 'Job', 'Country'

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


def startNode(node):

    print("starting %s" % node)

    wol.wake_on_lan(node)

def startCluster():

    print("starting lenovo")

    wol.wake_on_lan("lenovo")

    print("starting horus")

    wol.wake_on_lan("horus")



if __name__ == '__main__':

   root = Tk()

   ents = makeform(root, fields)

   root.bind('<Return>', (lambda event, e=ents: fetch(e)))

   b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)

   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)

   b3 = Button(root, text='Start lenovo', command=(lambda: startNode("lenovo")))
   b3.pack(side=LEFT, padx=5, pady=5)

   b4 = Button(root, text='Start cluster', command=(lambda: startCluster()))
   b4.pack(side=LEFT, padx=5, pady=5)


   root.mainloop()