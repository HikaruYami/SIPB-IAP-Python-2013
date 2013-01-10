class Database:
    def __init__(self):
      self.user_dict = {} #initialize the dictionary that will store all (user, password) pairs
    def add_user(self, username, pword):
      # Make sure the user does not already exist
      # if it does exist, add a new account to the dictionary
      # Returns True if a new account is made, False otherwise
      pass

    def change_pword(self, username, oldp, newp):
      # Two things must be true: the username must
      # already exist, and the old password must be right
      # If both are true, change the entry in self.user_dict
      # Returns True if the password is changed, False otherwise
      pass

    def access_acct(self, username, pword):
      # Again, the username must exist and the password
      # must be correct, but nothing is modified
      # Returns True if the account is accessed, False otherwise
      pass


db = database()

# Then you can run this type of thing from the interpreter:

db.add_user('fluffy', 'password123')
#returns True
db.add_user('fluffy', 'newpword')
#returns False
db.change_pword('hello?', 'password123', 'newpword')
#returns False
db.change_pword('fluffy', 'something', 'newpword')
#returns False
db.change_pword('fluffy', 'password123', 'newpword')
#returns True
db.access_acct('fluffy', 'password123')
#returns False
db.access_acct('who?', 'newpword')
#returns False
db.access_acct('fluffy', 'newpword')
#returns True
