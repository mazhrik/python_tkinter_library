dlist = [{'name': 'mun', }, {'name': 'haseeb'}]
class hello:
    def printtext(self):
        global e
        string = e.get()
        string2=e2.get()
        text.insert(INSERT, string)
        text.insert(INSERT, string2)
        for i in dlist:
            if i['name'] == string:
                i['name'] = string2
            else:
               pass
        print(dlist)


from tkinter import *
root = Tk()
obj=hello()
root.title('Name')
text = Text(root)
text2 = Text(root)
L1 = Label(root, text="User Name")
L1.pack()
e = Entry(root)
e.pack()
L2 = Label(root, text="User Name")
L2.pack()
e2 = Entry(root)
e2.pack()
e.focus_set()
e2.focus_set()
b = Button(root,text='click me to edit',command=obj.printtext)
text.pack
b.pack(side='bottom')
root.mainloop()