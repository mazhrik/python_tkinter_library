import random
import string
import datetime
from tkinter import *


class books:
    instances = dict()
    list = []

    def __init__(self, id, title, author, year, publisher, publisher_date, copies):
        self.id = id
        self.title = title
        self.year = year
        self.publisher = publisher
        self.publisher_date = publisher_date
        self.copies = copies
        self.author = author
        self.instances['id'] = id
        self.instances['title'] = title
        self.instances['author'] = author
        self.instances['year'] = year
        self.instances['publisher'] = publisher
        self.instances['publisher_date'] = publisher_date
        self.instances['copies'] = copies

    def display(self):
        print(self.id, self.title, self.author, self.year, self.publisher, self.publisher_date, self.copies)

    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def settitle(self, title):
        self.title = title

    def gettitle(self):
        return self.title

    def setauthor(self, author):
        self.author = author

    def getauthor(self):
        return self.author

    def setyear(self, year):
        self.year = year

    def getyear(self):
        return self.year

    def setpublisher(self, publisher):
        self.publisher = publisher

    def getpublisher(self):
        return self.publisher

    def setpublisher_date(self, publisher_date):
        self.publisher_date = publisher_date

    def getpublisher_date(self):
        return self.publisher_date

    def setcopies(self, copies):
        self.copies = copies

    def getcopies(self):
        return self.copies


class booklist(books):
    def __init__(self, id, title, author, year, publisher, publisher_date, copies):
        super().__init__(id, title, author, year, publisher, publisher_date, copies)

    def saving_record(self):
        x = books.instances
        books.list.append(dict(x))

    def deleting_record_(self, title):
        l = len(books.list)
        x = 0
        while x != l :
            if books.list[x]:
                if books.list[x]['title'] == title:
                    books.list[x].clear()
                    print('found,Deleted successfully \n')
                else:
                    pass
            else:
                pass
            x = x + 1

    def total_books(self):
        l = len(books.list)
        return print("-----------------total books------------->", l, 'Books')

    def display_record(self):
        print('book record ',books.list)
        return books.list

    def search_record(self, title):
        l = len(books.list)
        x = 0
        while x != l:
            if books.list[x]['title'] == title:
                print('----------------found successfully----------------- \n')
                return print(books.list[x])
                break
            else:
                pass
            x = x + 1
        print('------------No book found : Search operation failed ---------- \n')

    def editing_book_by_gui(self):
        global k
        string1 = k.get()
        string2 = e2.get()
        string3 = e3.get()
        string4 = e4.get()
        string5 = e5.get()
        string6 = e6.get()
        text.insert(INSERT, string1)
        text.insert(INSERT, string2)
        text.insert(INSERT, string3)
        text.insert(INSERT, string4)
        text.insert(INSERT, string5)
        text.insert(INSERT, string6)
        try:
            for b in books.list:
                if b['title'] == string1:
                    b['title'] = string2
                    b['author'] = string3
                    b['year'] = string4
                    b['publisher'] = string5
                    b['copies'] = string6
                else:
                    pass
        except Exception as e:
            print('------', e)
        print('updated')
        print(books.list)


class users:
    instance = dict()
    list2 = []

    def __init__(self, username, firstname, surname, housenumber, streetname, postcode, emailaddress, dateofbirth):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.housenumber = housenumber
        self.streetname = streetname
        self.postcode = postcode
        self.emailaddress = emailaddress
        self.dateofbirth = dateofbirth
        self.instance['username'] = username
        self.instance['firstname'] = firstname
        self.instance['surname'] = surname
        self.instance['housenumber'] = housenumber
        self.instance['streetname'] = streetname
        self.instance['postcode'] = postcode
        self.instance['emailaddress'] = emailaddress
        self.instance['dateofbirth'] = dateofbirth


class userlist(users):
    # def __init__(self, username, firstname, surname, housenumber, streetname, postcode, emailaddress, dateofbirth):
    #     super().__init__(username, firstname, surname, housenumber, streetname, postcode, emailaddress, dateofbirth)

    def savinng_users(self):
        x = users.instance
        users.list2.append(dict(x))

    def display_all_users(self):
        print('---user record---',users.list2)
        return users.list2

    def total_number_of_users(self):
        l = len(users.list2)
        return print("-----------------total user------------->", l, 'users')

    def search_user(self, firstname):
        l = len(users.list2)
        x = 0
        while x != l:
            if users.list2[x]['firstname'] == firstname:
                print('----------------found successfully----------------- \n')
                return print(users.list2[x])
                break
            else:
                pass
            x = x + 1
        print('------------No user found : Search operation failed ---------- \n')

    def deleting_user(self, firstname):
        ll = len(users.list2)
        k = 0
        while k != ll :
            if users.list2[k]:
                if users.list2[k]['firstname'] == firstname:
                    print('----------------user deleted successfully-------------')
                    users.list2[k].clear()
                else:
                    pass
            else:
                pass
            k = k + 1

    def edit_user(self, firstname, new_firstname, new_surname, new_dateofbirth, new_email):
        ll = len(users.list2)
        k = 0
        while k != ll:
            if users.list2[k]['firstname'] == firstname:
                users.list2[k]['firstname'] = new_firstname
                users.list2[k]['surname'] = new_surname
                users.list2[k]['dateofbirth'] = new_dateofbirth
                users.list2[k]['emailaddress'] = new_email
                print('-------------> Data updated SUCCESSFULLY')
            else:
                pass
            k = k + 1

    def printtext(self):
        global e
        string = e.get()
        string2 = e2.get()
        string3 = e3.get()
        string4 = e4.get()
        string5 = e5.get()
        text.insert(INSERT, string)
        text.insert(INSERT, string2)
        text.insert(INSERT, string3)
        text.insert(INSERT, string4)
        text.insert(INSERT, string5)
        for i in users.list2:
            if i['firstname'] == string:
                i['firstname'] = string2
                i['surname'] = string3
                i['dateofbirth'] = string4
                i['emailaddress'] = string5
            else:
                pass
        print(users.list2)

        # def editing_specific_user(self):
    #     l = len(users.list2)
    #     x = 0
    #     while x != l:
    #         if users.list2[x]['firstname'] == firstname:
    #             user2.list2[x]['firstname']
    #
    #             break
    #         else:
    #             pass
    #         x = x + 1
    #     print('------------No user found : Search operation failed ---------- \n')


class loans(books, users):
    # def __init__(self, id, title, author, year, publisher, publisher_date, copies):
    #     super().__init__(id, title, author, year, publisher, publisher_date, copies)
    books_borrowed = []

    def borrow_book(self):
        user_borrowing_the_book = input('enter the username of the user borrowing the book')
        title_of_book = input('enter  the title of the  book you wanna borrow')
        ll = len(users.list2)
        ll2 = len(books.list)
        k = 0
        m = 0
        dictionary = dict()
        try:
            while m != ll:
                if users.list2[m]['username'] == user_borrowing_the_book:
                    dictionary['user_borrowing'] = users.list2[m]['username']
                else:
                    pass
                m = m + 1
            while k != ll2:
                if books.list[k]['title'] == title_of_book:
                    dictionary['title_of_book'] = books.list[k]['title']
                else:
                    pass
                k = k + 1

            if dictionary['title_of_book'] and dictionary['user_borrowing']:
                print('dictionary->>', dictionary)
                loans.books_borrowed.append(dictionary)
                print('list of record')
                print(loans.books_borrowed)
                return (loans.books_borrowed)
            else:
                print('nothing found')
            # else:
            #     print(dictionary['title_of_book'])
            #
            #     print('--------->User_Name or Title of the book not found')

        except Exception as e:
            print('alert---------->', e)

    def returning_book(self):
        user_return = input('enter the user who wants to return the book')
        # ll = len(loans.books_borrowed)
        # i = 0
        try:
            for a in loans.books_borrowed:
                if a:
                    if a['user_borrowing'] == user_return:
                        a.clear()
                    else:
                        pass
                else:
                    pass
        except Exception as e:
            print('---error---', e)
        print(loans.books_borrowed)

    def counting_books_user_has(self):
        user_book = input('enter the name of  user for counting the number of books he has')
        # ll = len(loans.books_borrowed)
        i = 0
        try:
            for a in loans.books_borrowed:
                if a:
                    if a['user_borrowing'] == user_book:
                        i = i + 1
                    else:
                        pass
                else:
                    pass
        except Exception as e:
            print('---error---', e)
        print('this user has ', i, 'books')

# -------------------------------MAIN___FUNCTION----------------------------------------

xx = 0
while xx != 3:
    start_date = datetime.date(1999, 1, 1)
    end_date = datetime.date(2021, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    letters = string.ascii_lowercase
    id = random.randint(0, 10)
    title = ''.join(random.choice(letters) for i in range(5))
    author = ''.join(random.choice(letters) for i in range(10))
    year = random.randrange(1800, 2021, 5)
    publisher = ''.join(random.choice(letters) for i in range(5))
    publisher_date = random_date
    copies = random.randint(0, 100)
    ob = booklist(id, title, author, year, publisher, publisher_date, copies)
    ob.saving_record()
    start_date = datetime.date(1999, 1, 1)
    end_date = datetime.date(2021, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    letter = string.ascii_lowercase
    username = ''.join(random.choice(letter) for i in range(7))
    firstname = ''.join(random.choice(letter) for i in range(8))
    surname = ''.join(random.choice(letter) for i in range(5))
    housenumber = random.randint(0, 10)
    streetname = ''.join(random.choice(letter) for i in range(4))
    postcode = random.randint(0, 100)
    dateofbirth = random_date
    emailaddress = ''.join(random.choice(letter) for i in range(10))
    obj = userlist(username, firstname, surname, housenumber, streetname, postcode, emailaddress, dateofbirth)
    obj.savinng_users()
    obj2 = loans(id, title, author, year, publisher, publisher_date, copies)
    xx = xx + 1

x = 1
while x != 0:
    user = input(
        'Hey please enter \n 1 to display books \n 2 for total number of books \n 3 for deleting books \n 4 for searching book records \n 5 for displaying all users \n 6 for displaying total number of users \n 7 for deleting specific user \n 8 for searching a specific user \n 9 for edit a specific user \n 10 for borrowing a specific book \n 11 for counting the number of  books user has \n 12 for edit user from simple gui\n13 for editing the record of the book \n ')

    if user == '1':
        ob.display_record()
    elif user == '2':
        ob.total_books()
    elif user == '3':
        title_book1 = input('enter the title of book you wanna delete')
        ob.deleting_record_(title_book1)
    elif user == '4':
        title_book2 = input('enter the title of book you wanna search')
        ob.search_record(title_book2)
    elif user == '5':
        obj.display_all_users()
    elif user == '6':
        obj.total_number_of_users()
    elif user == '7':
        user_firstname1 = input('enter the firstname of the user you wanna delete')
        obj.deleting_user(user_firstname1)
    elif user == '8':
        user_firstname2 = input('enter the firstname of the user you wanna search')
        obj.search_user(user_firstname2)
    elif user == '9':
        user_firstname2 = input('enter the firstname of the user you wanna edit')
        new_firstname = input('enter new  firstname')
        new_surname = input('enter new  surname')
        new_dateofbirth = input('enter new  date of birth')
        new_email = input('enter new  email')
        obj.edit_user(user_firstname2, new_firstname, new_surname, new_dateofbirth, new_email)
    elif user == '10':
        obj2.borrow_book()
        u = input('do u wanna return the book enter 1 for yes and 2 for no')
        if u == '1':
            obj2.returning_book()
        else:
            pass
    elif user == '11':

        obj2.counting_books_user_has()
    elif user == '12':
        root = Tk()
        root.title('Name')
        text = Text(root)
        L1 = Label(root, text="FIRST NAME OF THE USER YOU WANNA EDIT")
        L1.pack()
        e = Entry(root,bd=5)
        e.pack()
        e.focus_set()
        L1 = Label(root, text="NEW FIRSTNAME")
        L1.pack()
        e2 = Entry(root,bd=5)
        e2.pack()
        e2.focus_set()
        L1 = Label(root, text="NEW SURNAME")
        L1.pack()
        e3 = Entry(root,bd=5)
        e3.pack()
        e3.focus_set()
        L1 = Label(root, text="NEW DATE OF BIRTH")
        L1.pack()
        e4 = Entry(root,bd=5)
        e4.pack()
        e4.focus_set()
        L1 = Label(root, text="NEW EMAIL")
        L1.pack()
        e5 = Entry(root,bd=5)
        e5.pack()
        e5.focus_set()
        b = Button(root, text='click me to edit', command=obj.printtext)
        text.pack
        b.pack(side='bottom')
        root.mainloop()
        print('hell')
    elif user == '13':
        root = Tk()
        root.title('Name')
        text = Text(root)
        L1 = Label(root, text="FIRST TITLE  OF THE BOOK YOU WANNA EDIT")
        L1.pack()
        k = Entry(root, bd=5)
        k.pack()
        k.focus_set()
        L1 = Label(root, text="NEW TITLE")
        L1.pack()
        e2 = Entry(root, bd=5)
        e2.pack()
        e2.focus_set()
        L1 = Label(root, text="NEW AUTHOR")
        L1.pack()
        e3 = Entry(root, bd=5)
        e3.pack()
        e3.focus_set()
        L1 = Label(root, text="NEW  YEAR")
        L1.pack()
        e4 = Entry(root, bd=5)
        e4.pack()
        e4.focus_set()
        L1 = Label(root, text="NEW PUBLISHER")
        L1.pack()
        e5 = Entry(root, bd=5)
        e5.pack()
        e5.focus_set()
        L1 = Label(root, text="NEW COPIES")
        L1.pack()
        e6 = Entry(root, bd=5)
        e6.pack()
        e6.focus_set()
        c = Button(root, text='click me to edit',command=ob.editing_book_by_gui)
        text.pack
        c.pack(side='bottom')
        root.mainloop()
        print('hell')


    x = x + 1
