import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class 

    Agrs:
    unittest.TestCase: Test class that defines test cases

    '''

    def setUp(self):
        '''
        This method runs before each test case 
        '''
        self.new_User = User("Lornakimani","kimanilorna@yahoo.com","psd123")
    def tearDown(self):
        '''
        This method cleans up after each case 
        '''
        User.Users=[]

    def test_init(self):
        '''
         This test case is to test if the object is intiniated properly 
        '''
        self.assertEqual(self.new_User.username,"Lornakimani")
        self.assertEqual(self.new_User.email,"kimanilorna@yahoo.com")
        self.assertEqual(self.new_User.password,"psd123")

    def test_add_user (self):
        '''
        This to test whether a user has been added to the users array
        '''
        self.new_User.add_user()
        self.assertEqual(len(User.Users),1)

    def test_save_multiple_users(self):
        '''
        Test to see if we can add multiple contacts
        '''
        self.new_User.add_user()
        multiple_user= User("ian","tuukuoian@yahoo.com","psd123")
        multiple_user.add_user()
        self.assertEqual(len(User.Users),2)

    def test_find_user(self):
        '''
        Test to see if other users can be found 
        '''
        self.new_User.add_user()
        test_user= User("ian","tuukuoian@yahoo.com","psd123")
        test_user.add_user()

        found_user=User.find_user("tuukuoian@yahoo.com","psd123")

        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists (self):

        '''
        test to see if we can find a user
        '''

        self.new_User.add_user()
        multiple_user= User("ian","tuukuoian@yahoo.com","psd123")
        multiple_user.add_user()

        user_exists = User.user_exists("ian")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.Users)
     
    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_User.add_user()
        User.copy_email("tuukuoian@yahoo.com","psd123")

        self.assertEqual(self.new_User.email, pyperclip.paste())




if __name__ == '__main__':
    unittest.main()