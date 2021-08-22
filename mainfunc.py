
def func():
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
            'Hey please enter \n 1 to display books \n 2 for total number of books \n 3 for deleting books \n 4 for searching book records \n 5 for displaying all users \n 6 for displaying total number of users \n 7 for deleting specific user \n 8 for searching a specific user \n 9 for edit a specific user \n 10 for borrowing a specific book \n 11 for counting the number of  books user has \n 12 for edit user from simple gui\n13 for editing the record of the book \n0 for exit  ')

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
