import unittest
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
        self.add_User = User("Lornakimani","kimanilorna@yahoo.com","psd123")
    def tearDown(self):
        '''
        This method cleans up after each case 
        '''
        User.users=[]

    def test_init(self):
        '''
         This test case is to test if the object is intiniated properly 
        '''
        self.assertEqual(self.add_User.username,"Lornakimani")
        self.assertEqual(self.add_User.email,"kimanilorna@yahoo.com")
        self.assertEqual(self.add_User.password,"psd123")

if __name__ == '__main__':
    unittest.main()