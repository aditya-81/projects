class UserData:
    def __init__(self):

        self.first_name = None
        self.last_name = None
        self.email = None
        self.phone_number = None
        self.re_enter_email = None
        self.input()

    def input(self):
        self.first_name = input("Enter Your First Name")
        self.last_name = input("Enter Your Last Name")
        while True:
            self.email = input("Enter Your Email")
            self.re_enter_email = input("Enter email again")
            if self.email == self.re_enter_email:
                print("Congrats!! You are added to the Trip Club")
                break
            else:
                print('Oops email does not match')
