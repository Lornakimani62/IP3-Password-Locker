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
    
    