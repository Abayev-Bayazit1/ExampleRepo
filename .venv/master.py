from database import Database





class System(object):

    def __init__(self,db):
        self.db = db


    def login(self):
        print("\nEnter username and password")
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        user  = self.db.get_user(name,password)

        if user:
            print(f"Login completed! Welcome,{user[0]}.Your role is {user[1]}")
        else:
            print("Login failed")



    def register(self):
        print("\nEnter your login details")

        try:
            name = input("Enter your name : ")
            password = input("Enter your password : ")
            role =input("Enter your role : ")

            if self.db.add_user(name,password,role):
                print("✅ Registered successfully")
            else:
                print("❌ User already exists" )

        except ValueError:
            print("\nEnter correct login details")




def main():
    db = Database()
    system = System(db)



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
            db.close()
            break

        else:
            print("Invalid choice")




if __name__ == '__main__':
    main()