import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    """ Test class for defining test cases for credential behavior """

    def setUp(self):
        """runs before each credential test case"""

        self.new_credential = Credential("facebook", "lornakimani", "psd123")

    def tearDown(self):
        """ Runs after each credential test case"""

        Credential.Accounts = []

    def test_init(self):
        """ Test whether credential objects are initialized properly """

        self.assertEqual(self.new_credential.platform, "facebook")
        self.assertEqual(self.new_credential.platform_username, "lornakimani")
        self.assertEqual(self.new_credential.platform_password, "psd123")

    def test_add_credentials(self):
        """ test whether new credential is added to Accounts list """

        self.new_credential.add_credentials()

        self.assertEqual(len(Credential.Accounts), 1)

    def test_save_multiple_credentials(self):
        """ test whether multiple users can be stored """

        self.new_credential.add_credentials()
        other_credential= Credential("Twitter", "kim", "password123")
        other_credential.add_credentials()
        self.assertEqual(len(Credential.Accounts),2)

    def test_find_credential(self):
        """ test whether credential can be found by platform """

        self.new_credential.add_credentials()
        other_credential = Credential("Twitter", "kim", "password123")

        other_credential.add_credentials()

        retrieved_credential = Credential.find_credential("Twitter")

        self.assertEqual(retrieved_credential.platform, other_credential.platform)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.add_credentials()
        other_credential= Credential("Twitter", "kim", "password123")
        other_credential.add_credentials()

        credential_exists = Credential.credential_exist("Twitter")

        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.Accounts)



if __name__ == '__main__':
    unittest.main()