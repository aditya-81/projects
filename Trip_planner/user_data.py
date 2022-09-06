
class UserData:
    def __init__(self):

        self.first_name = None
        self.last_name = None
        self.email = None
        self.phone_number = None
        self.re_enter_email = None

    def input(self,first_name,last_name,email,number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = number
