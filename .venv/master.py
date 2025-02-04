from wsgiref.validate import check_iterator

from abc import ABC, abstractmethod


class System(object):

    def __init__(self):
        self.users = []


    def login(self):
        print("\nEnter username and password")
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user["name"] == name and user["password"] == password:
                print("Login Successful,your role is {user['role']}")
                return

        print("Incorrect username or password")


    def register(self):
        print("\nEnter your login details")

        try:
            name = input("Enter your name : ")
            password = input("Enter your password : ")
            role =input("Enter your role : ")


            for user in self.users:
                if user.name == name:
                     print("\nUser already exists")
                else:
                    self.users.append({"name":name,"password":password,"role":role})
                    print("\nRegistered successfully")


        except ValueError:
            print("\nEnter correct login details")





def main():

    system = System()

    while True:
        print("[1].Login ")
        print("[2].Register ")
        print("[3].Exit")

        try:
            choise = int(input("Enter your choice : "))

        except ValueError:
            print("\n Choice should be an integer")

        if choise == 1:
            system.login()


        elif choise == 2:
            system.register()


        elif choise == 3:
            print("Exitting from the application...")
            break


        else:
            print("Invalid choice")




if __name__ == '__main__':
    main()