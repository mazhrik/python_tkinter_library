import unittest
from assingment import users, userlist, books, booklist, loans


class testfunctions(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_book(self):
        obj = books(22, 'first_book', 'author', 2003, 'publisher', 2 - 2 - 1999, 44)
        response_recieved = obj.title
        response_expected = 'first_book'
        self.assertEqual(response_recieved, response_expected)

    def test_user(self):
        obj = users('first_user', 'firstname', 'surname', 324, 'streetname', 123, 'emailaddress', 1 - 2 - 199)
        response_recieved = obj.username
        response_expected = 'first_user'
        self.assertEqual(response_recieved, response_expected)

    def test_userlist(self):
        obj = userlist('first_user', 'kamal', 'khan', 324, 'khi', 123, 'khan@gmail.com', 1 - 2 - 1999)
        obj2 = userlist('second_user', 'hamid', 'malik', 34, 'bayy', 123, 'seci@gmail.com', 1 - 2 - 1998)
        obj.savinng_users()
        obj.display_all_users()
        obj2.savinng_users()
        new_list = list(obj2.display_all_users())
        self.assertEqual(new_list[0]['firstname'], 'kamal')

    def test_booklist(self):
        obj = booklist(2, 'booktittle', 'author', 2021, 'publisher', 1-1-2020, 1122)
        obj.saving_record()
        new_lis2=obj.display_record()
        self.assertEqual(new_lis2[0]['title'], 'booktittle')



    def test_loan(self):
        obj2=booklist(2, 'booktittle', 'author', 2021, 'publisher', 1-1-2020, 1122)
        obj2.saving_record()
        obj = userlist('first_user', 'kamal', 'khan', 324, 'khi', 123, 'khan@gmail.com', 1 - 2 - 1999)
        obj.savinng_users()
        ob=loans(2, 'booktittle', 'author', 2021, 'publisher', 1-1-2020, 1122)
        new_list2=ob.borrow_book()
        self.assertEqual(new_list2[0]['user_borrowing'],'first_user')



if __name__ == '__main__':
    unittest.main()
