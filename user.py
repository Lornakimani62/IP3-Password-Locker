import pyperclip
from credentials import Credential

class User:

    """
    Class that generates instances of User's accounts and their passwords 
    """

    Users=[] #An array to hold user details

    username=''
    email=''
    password=''

    def __init__(self,username,email,password):
        
        self.username=username
        self.email=email
        self.password=password

    def add_user(self):

        '''
        Adds new user objects to the users array
        '''

        User.Users.append(self)

    @classmethod
    def find_user(cls,string,secret):
        '''
        Method that takes in a string and returns a user that matches that string
        Agrs:
            string: username to search for 
        Returns:
            user with the same username
        '''
        for User in cls.Users:
            if User.email == string and User.password == secret:

                return User

    @classmethod
    def user_exists(cls,string):
        '''
        Method that checks if a user exists
        Agrs:
            string: username to search for 
        Returns:
            True or false depending on whether the user exists 
        '''
        for User in cls.Users:
            if User.username == string:

                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.Users
    
    @classmethod
    def copy_email(cls,string,secret):
        found_user = User.find_user(string,secret)
        pyperclip.copy(found_user.email)

    
    