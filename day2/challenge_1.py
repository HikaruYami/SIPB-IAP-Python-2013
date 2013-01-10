class database:
    user_dict = {}
    def add_user(self, username, pword):
        if (username in self.user_dict):
            print "User exists!"
            return False
        self.user_dict[username] = pword
        print "Success!"
        return True
    def change_pword(self, username, oldp, newp):
        if (username not in self.user_dict):
            print "User does not exist!"
            return False
        elif self.user_dict[username] != oldp:
            print "Password is incorrect!"
            return False
        self.user_dict[username] = newp
        print "Success!"
        return True
    def access_acct(self, username, pword):
        if (username not in self.user_dict):
            print "User does not exist!"
            return False
        elif self.user_dict[username] != pword:
            print "Password is incorrect!"
            return False
        print "Success!"
        return True

db = database()
